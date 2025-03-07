import requests
import frappe

@frappe.whitelist()
def import_books(title, num_books):
    """Imports up to 20 books from the Frappe Library API and creates Book records in Frappe."""
    
    try:
        num_books = int(num_books) 

        if num_books > 20:
            frappe.throw("You can import a maximum of 20 books at a time.")

        API_URL = f"https://frappe.io/api/method/frappe-library?title={title}&limit={num_books}"

        response = requests.get(API_URL, headers={"Accept": "application/json"})
        response.raise_for_status()  

        data = response.json()
        if not isinstance(data, dict) or "message" not in data:
            frappe.throw("API returned unexpected data format.")

        books = data["message"]
        if not isinstance(books, list) or not books:
            return {"message": "No books found for the given title."}

        imported_count = 0

        for book in books:
            if not isinstance(book, dict):
                continue

            book_name = book.get("title", "Unknown")
            isbn = book.get("isbn", "")

            if frappe.db.exists("Book", {"book_name": book_name}) or (isbn and frappe.db.exists("Book", {"isbn": isbn})):
                continue

            doc = frappe.get_doc({
                "doctype": "Book",
                "book_name": book_name,
                "author": book.get("authors", "Unknown"),
                "isbn": isbn,
                "price": book.get("price", 0),
                "publisher": book.get("publisher", "Unknown"),
                "publication_year": book.get("publication_date", ""),
                "pages": book.get("num_pages", 0),
                "book_image": book.get("cover_image", ""),
                "stock": 10 
            })
            doc.insert(ignore_permissions=True)
            imported_count += 1

        return {"message": f"{imported_count} books imported successfully"}

    except ValueError:
        frappe.throw("Invalid number of books. Please enter a valid number.")

    except requests.exceptions.RequestException as e:
        frappe.throw(f"Failed to fetch books: {str(e)}")

    except Exception as e:
        frappe.throw(f"An unexpected error occurred: {str(e)}")

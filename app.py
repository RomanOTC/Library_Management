import tkinter as tk
from tkinter import messagebox, ttk
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["library_management"]  # New database name
books_collection = db["books"]      # Collection for books
members_collection = db["members"]   # Collection for library members
loans_collection = db["loans"]       # Collection for loans
returns_collection = db["returns"]    # Collection for returns

# Main Application Class
class LibraryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("700x600")
        self.root.config(bg="#34495E")
       
        self.create_widgets()
   
    def create_widgets(self):
        # Create Tabs
        self.tab_control = ttk.Notebook(self.root)
       
        self.books_tab = ttk.Frame(self.tab_control)
        self.members_tab = ttk.Frame(self.tab_control)
        self.loans_tab = ttk.Frame(self.tab_control)
        self.returns_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.books_tab, text="Books")
        self.tab_control.add(self.members_tab, text="Members")
        self.tab_control.add(self.loans_tab, text="Loans")
        self.tab_control.add(self.returns_tab, text="Returns")
        self.tab_control.pack(expand=1, fill="both")

        self.create_books_tab()
        self.create_members_tab()
        self.create_loans_tab()
        self.create_returns_tab()

    def create_books_tab(self):
        # Book Management Widgets
        tk.Label(self.books_tab, text="Book Title", bg="#34495E", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.book_title_entry = tk.Entry(self.books_tab, bg="#2C3E50", fg="white")
        self.book_title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.books_tab, text="Author", bg="#34495E", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.book_author_entry = tk.Entry(self.books_tab, bg="#2C3E50", fg="white")
        self.book_author_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.books_tab, text="ISBN", bg="#34495E", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.book_isbn_entry = tk.Entry(self.books_tab, bg="#2C3E50", fg="white")
        self.book_isbn_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.books_tab, text="Add Book", command=self.add_book, bg="#27AE60", fg="black").grid(row=3, column=0, padx=5)
        tk.Button(self.books_tab, text="View Books", command=self.view_books, bg="#2980B9", fg="black").grid(row=3, column=1, padx=5)

        self.books_tree = ttk.Treeview(self.books_tab, columns=("Title", "Author", "ISBN"), show="headings")
        self.books_tree.heading("Title", text="Book Title")
        self.books_tree.heading("Author", text="Author")
        self.books_tree.heading("ISBN", text="ISBN")
        self.books_tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def create_members_tab(self):
        # Member Management Widgets
        tk.Label(self.members_tab, text="Member Name", bg="#34495E", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.member_name_entry = tk.Entry(self.members_tab, bg="#2C3E50", fg="white")
        self.member_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.members_tab, text="Member ID", bg="#34495E", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.member_id_entry = tk.Entry(self.members_tab, bg="#2C3E50", fg="white")
        self.member_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.members_tab, text="Email", bg="#34495E", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.member_email_entry = tk.Entry(self.members_tab, bg="#2C3E50", fg="white")
        self.member_email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.members_tab, text="Add Member", command=self.add_member, bg="#27AE60", fg="black").grid(row=3, column=0, padx=5)
        tk.Button(self.members_tab, text="View Members", command=self.view_members, bg="#2980B9", fg="black").grid(row=3, column=1, padx=5)

        self.members_tree = ttk.Treeview(self.members_tab, columns=("Name", "ID", "Email"), show="headings")
        self.members_tree.heading("Name", text="Member Name")
        self.members_tree.heading("ID", text="Member ID")
        self.members_tree.heading("Email", text="Email")
        self.members_tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def create_loans_tab(self):
        # Loan Management Widgets
        tk.Label(self.loans_tab, text="Member ID", bg="#34495E", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.loan_member_id_entry = tk.Entry(self.loans_tab, bg="#2C3E50", fg="white")
        self.loan_member_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.loans_tab, text="Book ISBN", bg="#34495E", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.loan_book_isbn_entry = tk.Entry(self.loans_tab, bg="#2C3E50", fg="white")
        self.loan_book_isbn_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.loans_tab, text="Loan Date", bg="#34495E", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.loan_date_entry = tk.Entry(self.loans_tab, bg="#2C3E50", fg="white")
        self.loan_date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.loans_tab, text="Add Loan", command=self.add_loan, bg="#27AE60", fg="black").grid(row=3, column=0, padx=5)
        tk.Button(self.loans_tab, text="View Loans", command=self.view_loans, bg="#2980B9", fg="black").grid(row=3, column=1, padx=5)

        self.loans_tree = ttk.Treeview(self.loans_tab, columns=("Member ID", "Book ISBN", "Loan Date"), show="headings")
        self.loans_tree.heading("Member ID", text="Member ID")
        self.loans_tree.heading("Book ISBN", text="Book ISBN")
        self.loans_tree.heading("Loan Date", text="Loan Date")
        self.loans_tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def create_returns_tab(self):
        # Return Management Widgets
        tk.Label(self.returns_tab, text="Loan ID", bg="#34495E", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.return_loan_id_entry = tk.Entry(self.returns_tab, bg="#2C3E50", fg="white")
        self.return_loan_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.returns_tab, text="Return Date", bg="#34495E", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.return_date_entry = tk.Entry(self.returns_tab, bg="#2C3E50", fg="white")
        self.return_date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.returns_tab, text="Add Return", command=self.add_return, bg="#27AE60", fg="black").grid(row=2, column=0, padx=5)
        tk.Button(self.returns_tab, text="View Returns", command=self.view_returns, bg="#2980B9", fg="black").grid(row=2, column=1, padx=5)

        self.returns_tree = ttk.Treeview(self.returns_tab, columns=("Loan ID", "Return Date"), show="headings")
        self.returns_tree.heading("Loan ID", text="Loan ID")
        self.returns_tree.heading("Return Date", text="Return Date")
        self.returns_tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_book(self):
        book_title = self.book_title_entry.get()
        book_author = self.book_author_entry.get()
        book_isbn = self.book_isbn_entry.get()
       
        if not book_title or not book_author or not book_isbn:
            messagebox.showwarning("Warning", "All fields are required to add a book.")
            return

        books_collection.insert_one({"title": book_title, "author": book_author, "isbn": book_isbn})
        messagebox.showinfo("Success", "Book added successfully.")
        self.book_title_entry.delete(0, tk.END)
        self.book_author_entry.delete(0, tk.END)
        self.book_isbn_entry.delete(0, tk.END)

    def view_books(self):
        for row in self.books_tree.get_children():
            self.books_tree.delete(row)
       
        for book in books_collection.find():
            self.books_tree.insert("", "end", values=(book["title"], book["author"], book["isbn"]))

    def add_member(self):
        member_name = self.member_name_entry.get()
        member_id = self.member_id_entry.get()
        member_email = self.member_email_entry.get()

        if not member_name or not member_id or not member_email:
            messagebox.showwarning("Warning", "All fields are required to add a member.")
            return

        members_collection.insert_one({"name": member_name, "member_id": member_id, "email": member_email})
        messagebox.showinfo("Success", "Member added successfully.")
        self.member_name_entry.delete(0, tk.END)
        self.member_id_entry.delete(0, tk.END)
        self.member_email_entry.delete(0, tk.END)

    def view_members(self):
        for row in self.members_tree.get_children():
            self.members_tree.delete(row)

        for member in members_collection.find():
            self.members_tree.insert("", "end", values=(member["name"], member["member_id"], member["email"]))

    def add_loan(self):
        member_id = self.loan_member_id_entry.get()
        book_isbn = self.loan_book_isbn_entry.get()
        loan_date = self.loan_date_entry.get()

        if not member_id or not book_isbn or not loan_date:
            messagebox.showwarning("Warning", "All fields are required to add a loan.")
            return

        loans_collection.insert_one({"member_id": member_id, "book_isbn": book_isbn, "loan_date": loan_date})
        messagebox.showinfo("Success", "Loan added successfully.")
        self.loan_member_id_entry.delete(0, tk.END)
        self.loan_book_isbn_entry.delete(0, tk.END)
        self.loan_date_entry.delete(0, tk.END)

    def view_loans(self):
        for row in self.loans_tree.get_children():
            self.loans_tree.delete(row)

        for loan in loans_collection.find():
            self.loans_tree.insert("", "end", values=(loan["member_id"], loan["book_isbn"], loan["loan_date"]))

    def add_return(self):
        loan_id = self.return_loan_id_entry.get()
        return_date = self.return_date_entry.get()

        if not loan_id or not return_date:
            messagebox.showwarning("Warning", "All fields are required to add a return.")
            return

        returns_collection.insert_one({"loan_id": loan_id, "return_date": return_date})
        messagebox.showinfo("Success", "Return added successfully.")
        self.return_loan_id_entry.delete(0, tk.END)
        self.return_date_entry.delete(0, tk.END)

    def view_returns(self):
        for row in self.returns_tree.get_children():
            self.returns_tree.delete(row)

        for return_ in returns_collection.find():
            self.returns_tree.insert("", "end", values=(return_["loan_id"], return_["return_date"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementApp(root)
    root.mainloop()

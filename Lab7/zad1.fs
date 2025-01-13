open System

type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages
    member this.GetInfo() = sprintf "Tytuł: %s, Autor: %s, Liczba stron: %d" title author pages

type User(name: string) =
    let mutable borrowedBooks = []
    member this.Name = name
    member this.BorrowBook(book: Book) =
        borrowedBooks <- book :: borrowedBooks
        printfn "%s wypożyczył książkę: %s" name book.Title
    member this.ReturnBook(book: Book) =
        if List.contains book borrowedBooks then
            borrowedBooks <- List.filter ((<>) book) borrowedBooks
            printfn "%s zwrócił książkę: %s" name book.Title
        else
            printfn "Książka %s nie została wypożyczona przez %s." book.Title name
    member this.ListBorrowedBooks() =
        if borrowedBooks.IsEmpty then
            printfn "%s nie ma wypożyczonych książek." name
        else
            printfn "Książki wypożyczone przez %s:" name
            borrowedBooks |> List.iter (fun book -> printfn "  %s" (book.GetInfo()))

type Library() =
    let mutable books = []
    member this.AddBook(book: Book) =
        books <- book :: books
        printfn "Dodano książkę: %s" book.Title
    member this.RemoveBook(book: Book) =
        if List.contains book books then
            books <- List.filter ((<>) book) books
            printfn "Usunięto książkę: %s" book.Title
        else
            printfn "Książka %s nie znajduje się w bibliotece." book.Title
    member this.ListBooks() =
        if books.IsEmpty then
            printfn "Biblioteka jest pusta."
        else
            printfn "Książki w bibliotece:"
            books |> List.iter (fun book -> printfn "  %s" (book.GetInfo()))
    member this.BorrowBook(book: Book, user: User) =
        if List.contains book books then
            this.RemoveBook(book)
            user.BorrowBook(book)
        else
            printfn "Książka %s nie jest dostępna w bibliotece." book.Title
    member this.ReturnBook(book: Book, user: User) =
        user.ReturnBook(book)
        this.AddBook(book)

let main () =
    let library = Library()
    let user = User("Jan Kowalski")
    let book1 = Book("Wiedźmin", "Andrzej Sapkowski", 320)
    library.AddBook(book1)
    library.ListBooks()
    library.BorrowBook(book1, user)
    library.ListBooks()
    user.ListBorrowedBooks()
    library.ReturnBook(book1, user)
    library.ListBooks()

main ()
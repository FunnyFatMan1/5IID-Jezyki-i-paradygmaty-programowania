open System

type BankAccount(accountNumber: string, initialBalance: decimal) =
    let mutable balance = initialBalance
    member this.AccountNumber = accountNumber
    member this.Balance = balance
    member this.Deposit(amount: decimal) =
        if amount > 0m then
            balance <- balance + amount
            printfn "Wpłacono: %.2f, Nowe saldo: %.2f" amount balance
        else
            printfn "Kwota wpłaty musi być większa od zera."
    member this.Withdraw(amount: decimal) =
        if amount > 0m && amount <= balance then
            balance <- balance - amount
            printfn "Wypłacono: %.2f, Nowe saldo: %.2f" amount balance
        elif amount > balance then
            printfn "Niewystarczające środki na koncie."
        else
            printfn "Kwota wypłaty musi być większa od zera."

type Bank() =
    let mutable accounts = Map.empty<string, BankAccount>
    member this.CreateAccount(accountNumber: string, initialBalance: decimal) =
        if accounts.ContainsKey(accountNumber) then
            printfn "Konto z numerem %s już istnieje." accountNumber
        else
            let account = BankAccount(accountNumber, initialBalance)
            accounts <- accounts.Add(accountNumber, account)
            printfn "Utworzono konto z numerem: %s, Saldo początkowe: %.2f" accountNumber initialBalance
    member this.GetAccount(accountNumber: string) =
        if accounts.ContainsKey(accountNumber) then
            Some(accounts.[accountNumber])
        else
            printfn "Konto z numerem %s nie istnieje." accountNumber
            None
    member this.UpdateAccount(accountNumber: string, newBalance: decimal) =
        match this.GetAccount(accountNumber) with
        | Some(account) ->
            account.Deposit(newBalance - account.Balance)
            printfn "Zaktualizowano saldo konta %s do %.2f" accountNumber newBalance
        | None -> ()
    member this.DeleteAccount(accountNumber: string) =
        if accounts.ContainsKey(accountNumber) then
            accounts <- accounts.Remove(accountNumber)
            printfn "Usunięto konto z numerem: %s" accountNumber
        else
            printfn "Konto z numerem %s nie istnieje." accountNumber
    member this.ListAccounts() =
        if accounts.IsEmpty then
            printfn "Brak kont w banku."
        else
            printfn "Lista kont w banku:"
            accounts
            |> Map.iter (fun key account ->
                printfn "  Numer konta: %s, Saldo: %.2f" account.AccountNumber account.Balance)

let main () =
    let bank = Bank()
    bank.CreateAccount("123", 1000m)
    bank.CreateAccount("456", 500m)
    bank.ListAccounts()
    match bank.GetAccount("123") with
    | Some(account) -> account.Deposit(200m)
    | None -> ()
    match bank.GetAccount("123") with
    | Some(account) -> account.Withdraw(300m)
    | None -> ()
    bank.UpdateAccount("456", 1000m)
    bank.DeleteAccount("123")
    bank.ListAccounts()

main ()

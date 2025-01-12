open System


let przeksztalcFormat (wpis: string) : string =
    let dane = wpis.Split(';') |> Array.map (fun s -> s.Trim())
    if dane.Length = 3 then
        let imie = dane.[0]
        let nazwisko = dane.[1]
        let wiek = dane.[2]
        sprintf "%s, %s (%s lat)" nazwisko imie wiek
    else
        "Nieprawidłowy format danych"


let main () =
    printf "Podaj wpisy w formacie \"imię; nazwisko; wiek\" oddzielone nową linią. Zakończ wprowadzanie pustą linią:\n"
    let rec czytajWpisy (akumulator: string list) =
        let linia = Console.ReadLine()
        if String.IsNullOrWhiteSpace(linia) then
            akumulator
        else
            czytajWpisy (linia :: akumulator)
    let wpisy = czytajWpisy [] |> List.rev
    let przetworzone = wpisy |> List.map przeksztalcFormat
    printfn "\nPrzetworzone dane:"
    przetworzone |> List.iter (printfn "%s")


main ()
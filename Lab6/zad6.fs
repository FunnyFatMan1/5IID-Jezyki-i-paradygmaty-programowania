open System


let zamienSlowo (tekst: string) (doZamiany: string) (noweSlowo: string) =
    tekst.Replace(doZamiany, noweSlowo)


let main () =
    printf "Podaj tekst: "
    let tekst = Console.ReadLine()
    printf "Podaj słowo, które chcesz zamienić: "
    let doZamiany = Console.ReadLine()
    printf "Podaj nowe słowo: "
    let noweSlowo = Console.ReadLine()

    let zmodyfikowanyTekst = zamienSlowo tekst doZamiany noweSlowo
    printfn "\nZmieniony tekst: %s" zmodyfikowanyTekst


main ()
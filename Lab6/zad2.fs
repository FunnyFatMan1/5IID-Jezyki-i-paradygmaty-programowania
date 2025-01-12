open System


let czyPalindrom (tekst: string) =
    let odwrocony = new string(Array.rev (tekst.ToCharArray()))
    tekst = odwrocony


let main () =
    printf "Podaj tekst: "
    let tekst = Console.ReadLine()
    if czyPalindrom tekst then
        printfn "Podany tekst \"%s\" jest palindromem." tekst
    else
        printfn "Podany tekst \"%s\" nie jest palindromem." tekst


main ()

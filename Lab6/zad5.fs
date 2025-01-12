open System


let znajdzNajdluzszeSlowo (tekst: string) =
    tekst.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    |> Array.fold (fun (najdluzsze, maxDlugosc) slowo ->
        if slowo.Length > maxDlugosc then
            (slowo, slowo.Length)
        else
            (najdluzsze, maxDlugosc)
    ) ("", 0)


let main () =
    printf "Podaj tekst: "
    let tekst = Console.ReadLine()
    let (najdluzszeSlowo, dlugosc) = znajdzNajdluzszeSlowo tekst
    if najdluzszeSlowo = "" then
        printfn "Nie podano żadnych słów."
    else
        printfn "Najdłuższe słowo: \"%s\"" najdluzszeSlowo
        printfn "Długość najdłuższego słowa: %d" dlugosc


main ()
open System

let liczSlowa (tekst: string) =
    tekst.Split([| ' '; '\t'; '\n'; '\r' |], StringSplitOptions.RemoveEmptyEntries)
    |> Array.length


let liczZnakiBezSpacji tekst =
    tekst
    |> Seq.filter (fun c -> not (Char.IsWhiteSpace(c)))
    |> Seq.length


let main () =
    printf "Podaj tekst: "
    let tekst = Console.ReadLine()
    let liczbaSlow = liczSlowa tekst
    let liczbaZnakowBezSpacji = liczZnakiBezSpacji tekst
    printfn "Liczba słów: %d" liczbaSlow
    printfn "Liczba znaków (bez spacji): %d" liczbaZnakowBezSpacji

main ()
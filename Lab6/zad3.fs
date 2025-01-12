open System


let usunDuplikaty lista =
    lista |> List.distinct


let main () =
    printf "Podaj słowa oddzielone spacjami: "
    let input = Console.ReadLine()
    let slowa = input.Split(' ') |> Array.toList
    let unikalneSlowa = usunDuplikaty slowa
    printfn "Unikalne słowa: %A" unikalneSlowa


main ()
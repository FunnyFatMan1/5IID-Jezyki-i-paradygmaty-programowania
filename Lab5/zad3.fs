let rec permutacje lista =
    match lista with
    | [] -> [[]]
    | _ ->
        [for x in lista do
            let reszta = List.filter (fun y -> y <> x) lista
            for perm in permutacje reszta do
                yield x :: perm]


let lista = [1; 2; 3]
let wynik = permutacje lista
printfn "%A" wynik
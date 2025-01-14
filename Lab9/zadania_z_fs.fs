open System
 (*let rec silnia n=
    if n <0 then 0
    elif n=0 || n=1 then 1
    else n* silnia (n-1)

printf "Podaj liczbę: "
let liczba = Console.ReadLine() |> int
printf "silnia z liczby %d wynosi %d" liczba (silnia liczba)
*)

//Używając funkcji List.map, zamień wszystkie litery w liście słów na wielkie litery.

 (* let naWielkie (lista: string list)= List.map (fun slowo -> slowo.ToUpper())
let slowa = ["macijerze"; "z"; "liwa"; "do"; "priwa"]
printf "nowa lista : %A"  (naWielkie slowa)  

let naWielkie (lista: string list) =
    lista |> List.map (fun slowo -> slowo.ToUpper()) 

let slowa = ["maciejrze"; "z"; "liwa"; "do"; "priwa"]
let nowaLista = naWielkie slowa

printfn "Nowa lista: %A" nowaLista

*)

// Zaimplementuj algorytm znajdowania największego wspólnego dzielnika (NWD) dwóch liczb.
(*
let rec nwd x1 x2=
    if x1 <0  then 0 
    elif x2 =0 then x1 
    else nwd x2 (x2 % x1)


printf "nwd od tych liczb to: %d " (nwd 30 15 )
*)
   
//Stwórz program, który przekształca listę łańcuchów na listę ich długości, używając funkcji funkcyjnych.
(*
let dlugoscCiagu (lista:string list)=
    lista |> List.map (fun slowo->slowo.Length )

let przyklad =["jeden";"dwa";"trzy"]

printf "oto przyklad listy : %A" (dlugoscCiagu przyklad)
*)

//Napisz funkcję, która oblicza sumę liczb od 1 do n
 (*
 let suma n=
    let mutable pom = 0 
    for i in 1..n do
        pom <- pom + i
    pom

printf "podaj liczbe: "
let liczba= Console.ReadLine()  |> int 
printf "suma liczb od 1 do %d to: %d" liczba (suma liczba) 

 *)


 //obliczanie sumy liczb z listy
let rec sumaListy lista =
    match lista with
    | [] -> 0 // Pusta lista - suma to 0
    | head :: tail -> head + sumaListy tail // Dodaj pierwszy element do sumy reszty listy

let wynik = sumaListy [1; 2; 3; 4; 5]
printfn "Suma: %d" wynik

 
    

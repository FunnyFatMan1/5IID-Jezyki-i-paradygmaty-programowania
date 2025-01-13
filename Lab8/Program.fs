open System
open System.Collections.Generic

//definicja listy łączonej
type LinkedList<'T> =
    | Empty 
    | Node of 'T * LinkedList<'T>

let Head =
    function
    | Empty -> failwith "Nie można pobrać głowy z listy pustej"
    | Node(Head,_) -> Head

let Tail =
    function
    | Empty -> failwith "Nie można pobrać ogona z listy pustej"
    | Node(Tail,_) -> Tail

let addHead value list =
    Node(value, list)

let rec printList list =
    match list with 
    | Empty -> ()
    | Node(value, next) ->
        printf "%A " value
        printList next

let rec numberElements =
    function
    | Empty -> 0
    | Node(_, Tail) -> numberElements Tail + 1


[<EntryPoint>]
let main argv =
    let list1 = Empty
    let list2 = addHead 1 list1
    let list3 = addHead 2 list2
    let list4 = addHead 3 list3

    printList list4

    0
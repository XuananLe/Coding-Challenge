package main

import (
	"flag"
	"log"
	"os"
	"github.com/emirpasic/gods/v2/trees/binaryheap"
)

type Node struct {
	Char string
	Freq int
	Left *Node
	Right *Node
}

func nodeComparator(a, b interface{}) int {
	node_a := a.(*Node)
	node_b := b.(*Node)
	return node_a.Freq - node_b.Freq
}

func generateCode(node *Node, prefix string, codes map[string]string){
	if node == nil {
		return
	}
	if node.Left == nil && node.Right == nil {
		codes[node.Char] = prefix
	}
	generateCode(node.Left, prefix + "0", codes)
	generateCode(node.Right, prefix + "1", codes)
}

func main() {
	log.SetFlags(0)
	f := flag.String("f", "", "")
	flag.Parse()
	bytes, err := os.ReadFile(*f)
	if err != nil {
		log.Fatal(err)
	}
	data := string(bytes)
	occur := make(map[string]int)
	for _, c := range data {
		occur[string(c)] += 1
	}
	log.Println(occur["X"])
	log.Println(occur["t"])
	heap  := binaryheap.NewWith(nodeComparator)
	
	for ch, freq:= range occur {
		heap.Push(&Node {
			Char: ch,
			Freq: freq,
		})
	}	
	for heap.Size() > 1 {
		a, _ := heap.Pop()
		b, _ := heap.Pop()
		left := a.(*Node)
		right := b.(*Node)
		merged := &Node {
			Freq: left.Freq + right.Freq,
			Left: left,
			Right: right,
		}
		heap.Push(merged)
	}
	codes := make(map[string]string)
	root, _ := heap.Pop()
	generateCode(root.(*Node), "", codes)
    log.Println("Huffman Codes for each symbol:")
    for ch, code := range codes {
        log.Printf("  %q: %s\n", ch, code)
    }
	
}	
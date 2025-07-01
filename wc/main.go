package main

import (
	"bufio"
	"flag"
	"log"
	"os"
	"strings"
	"unicode/utf8"
)

type FileInfo struct {
	Bytes int
	Lines int
	Words int
	Characters int
	FileName string
}

func provideInfo(fileName string) (FileInfo,  error) {
	file, err := os.Open(fileName)
	if err != nil {
		return FileInfo{}, err
	}
	defer file.Close()
	
	bytes, lines, words, characters := 0, 0, 0, 0
	if tmp, err := os.Stat(fileName); err == nil {
		bytes = int(tmp.Size())
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines += 1
		words += len(strings.Fields(scanner.Text()))
		characters += utf8.RuneCountInString(scanner.Text())
	}
	return FileInfo{
		Bytes: bytes,
		Lines: lines,
		Words:  words,
		Characters: characters,
		FileName: fileName,
	}, nil 
}

func main() {
	log.SetFlags(0)
	log.SetPrefix("")
	c := flag.String("c", "", "")
	l := flag.String("l", "", "")
	w := flag.String("w", "", "")
	m := flag.String("m", "", "")
	flag.Parse()

	if *c == "" && *l == "" && *w == "" && *m == "" {
		args := os.Args
		if len(args) == 1{
			log.Fatal("Please provide input file")
		}
		if res, err := provideInfo(args[1]); err == nil {
			log.Println(res)
		}
	}

	if *c != "" {
		if res, err := provideInfo(*c); err == nil {
			log.Println(res.Bytes)
			log.Println(res.FileName)
		}
	}

	if *l != "" {
		if res, err := provideInfo(*l); err == nil {
			log.Println(res.Lines)
			log.Println(res.FileName)
		}
	}
	if *w != "" {
		if res, err := provideInfo(*w); err == nil {
			log.Println(res.Words)
			log.Println(res.FileName)
		}
	}
	if *m != "" {
		if res, err := provideInfo(*m); err == nil {
			log.Println(res.Characters)
			log.Println(res.FileName)
		}
	}

}

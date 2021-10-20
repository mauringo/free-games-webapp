package main

import (
        "net/http"
)

func main() {
        http.Handle("/", http.StripPrefix("/", http.FileServer(http.Dir("./static"))))
        http.ListenAndServe(":3001", nil)
}

package main

import (
    "fmt"
    "io"
    "os"
    "net/http"
)

const IndexHtml = `
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Upload File</title>
  </head>
  <body>
    <form
      enctype="multipart/form-data"
      action="/uploadFile"
      method="post"
    >
      <input type="file" name="myFile" />
      <input type="submit" value="upload" />
    </form>
  </body>
</html>
`

func display(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, IndexHtml)
}

func uploadFile(w http.ResponseWriter, r *http.Request) {
        // Maximum upload of 10 MB files
        r.ParseMultipartForm(10 << 20)

        // Get handler for filename, size and headers
        file, handler, err := r.FormFile("myFile")
        if err != nil {
                fmt.Println("Error Retrieving the File")
                fmt.Println(err)
                return
        }

        defer file.Close()
        fmt.Printf("Uploaded File: %+v\n", handler.Filename)
        fmt.Printf("File Size: %+v\n", handler.Size)
        fmt.Printf("MIME Header: %+v\n", handler.Header)

        // Create file
        dst, err := os.Create(handler.Filename)
        defer dst.Close()
        if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
        }

        // Copy the uploaded file to the created file on the filesystem
        if _, err := io.Copy(dst, file); err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
        }
        fmt.Fprintf(w, "Successfully Uploaded File\n")
}

func main() {
    http.HandleFunc("/uploadFile", uploadFile)
    http.HandleFunc("/upload", display)
    http.ListenAndServe(":8082", nil)
}

# PDF Web Toolkit

A Web-Application allowing you to split and merge PDF-Files.

## Deploy

Clone the repo and enter the directory. Than run the following:

    docker build -t pdf-web-toolkit .
    docker run -d --name pdf-web-toolkit -p 8002:8000 -i -t pdf-web-toolkit

Once finished, you should be able to connect to http://\<your-ip\>:8002




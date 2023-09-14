# dog-detector 
This is a project for dog-bark-detection and dog-inspired notification. There is a placeholder function that could send a message to a URL. Otherwise, it just prints out "Got one!" every time it hears a dog bark. 

## How to Use

1. Grab from github

`git clone https://github.com/owfinlay/dog-detector --depth=1`

2. Navigate to folder and build

`cd dog-detector`
`docker build . -t dog-det`

3. Run the following command

```
docker run --rm --device /dev/snd:/dev/snd dog-det:latest -d
```

There are two adjustable settings that you change via the `-e` flag, which stands for environment variable. These are `SENSITIVITY` and `DECISION THRESHOLD`; if you want to specify both, you can just repeat the `e` flag, like so: 

```
docker run -it --rm --device /dev/snd:/dev/snd dog-det:latest -d -e SENSITIVITY=5 -e "DECISION THRESHOLD"=8
```
# dog-detector 
This is a project for dog-bark-detection and dog-inspired notification. There is a placeholder function that could send a message to a URL. Otherwise, it just prints out "Got one!" every time it hears a dog bark. 

## How to Use

1. Grab from github
```
git clone https://github.com/owfinlay/dog-detector --depth=1
```

2. Navigate to folder and build
```
cd dog-detector
docker build . -t dog-det
```

3. Run the following command

```
docker run -it --device /dev/snd:/dev/snd dog-det:latest
```

Here are some explanations of flags you might find relevant:

- `--rm` deletes the container as soon as it's finished running, which is nice for cleanup.
- `--device` specifies a device to connect through your machine's OS to the container's OS. Here, it is used to mount the `/dev/snd` file which is where audio devices appear on Linux.
- `--env` / `-e` allows you to set environment variables. If you want to set multiple, you can just use it multiple times (`... -e SENSITIVITY=6 -e "DECISION THRESHOLD"=4`).
  - The two current options for environment variables must be typed in all caps like in the example.
- `-it` allows you to interact with the running container via a shell-like interface.
- `-d` stands for detach, and allows the program to run in the background. Obviously you wouldn't want to use this and `-it` at once.


These are the flags that seem useful, you can look through more flags [here](https://docs.docker.com/engine/reference/commandline/run/).
FROM gcc:latest AS build

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/Dxftoro/Lnshell-nerfed.git /src/

WORKDIR /src/
RUN gcc -o output ./*.c

FROM alpine:latest AS final
RUN apk add gcompat

WORKDIR /app/
COPY --from=build /src/output /app/
COPY --from=build /src/result.txt /app/
RUN chmod +x /app/output

CMD ["./output"]

FROM python:3.6.6-alpine3.6

RUN apk update && apk add bash gcc libffi-dev libc-dev openssl-dev
COPY sampleapp /sampleapp
WORKDIR /sampleapp
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
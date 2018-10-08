FROM python:3.6.6-alpine3.6

RUN apk update && apk add bash
COPY sampleapp /sampleapp
WORKDIR /sampleapp
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
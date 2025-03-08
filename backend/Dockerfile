FROM python:3.12-slim

# Setting resource quota
ARG MIN_MEM=2G
ARG MAX_MEM=2G

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv
RUN uv pip install poetry --system
RUN poetry install --no-interaction --no-ansi
EXPOSE 8000

#Execution
CMD [ "poetry", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

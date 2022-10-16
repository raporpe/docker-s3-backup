FROM python:alpine

# Create directory where the files to backup are mapped
RUN mkdir /backup

WORKDIR /usr/src/app

COPY requirements.txt .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x configure-cron.sh

CMD [ "./configure-cron.sh" ]
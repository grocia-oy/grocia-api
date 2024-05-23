ENV_FILE="./.env"

compose_up:
	source ${ENV_FILE} && docker-compose up -d

compose_down:
	source ${ENV_FILE} && docker-compose down
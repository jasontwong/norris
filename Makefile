NAME="norris-slack-bot"

all : build

build :
	docker build -t $(NAME) .

shell :
	docker run --rm -it \
	-v `pwd`:/code \
  -e ALGOLIA_APP_ID=$(ALGOLIA_APP_ID) \
  -e ALGOLIA_API_KEY=$(ALGOLIA_API_KEY) \
	$(NAME) bash

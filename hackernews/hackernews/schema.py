import graphene

import links.schema

class Query(links.schema.Query, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)

class CreateLink(graphene.Mutation):
  id = graphene.Int()
  url = graphene.String()
  description = graphene.String()

  class Arguments:
    url = graphene.String()
    description = graphene.String()

    def mutate(self, info, url, description):
      link = Link(url=url, description=description)
      link.save()

      return CreateLink(
        id=link.id,
        url=link.url,
        description=link.description,
      )

class Mutation(graphene.ObjectType):
  create_link = CreateLink.Field()
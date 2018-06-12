import graphene
from graphene import relay, String
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from infoset.db.db_orm import db_session, Datapoint as DatapointModel


class Datapoint(SQLAlchemyObjectType):
    class Meta:
        model = DatapointModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_datapoints = SQLAlchemyConnectionField(Datapoint)
    hello = String(description='Hello')
    def resolve_hello(self, args, context, info):
        return 'World'

schema = graphene.Schema(query=Query)
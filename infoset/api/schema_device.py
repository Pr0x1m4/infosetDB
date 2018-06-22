import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from infoset.api import graphene_utils
from infoset.db.db_orm import db_session, Device as DeviceModel
from datetime import datetime

class DeviceAttribute:
    
    idx_device =  graphene.ID(description="")
    devicename = graphene.String(description="")
    description = graphene.String(description="")
    enabled = graphene.Float(description="")
    ts_modified = graphene.DateTime(description="")
    ts_created = graphene.DateTime(description="")


class Device(SQLAlchemyObjectType, DeviceAttribute):
    class Meta:
        model = DeviceModel
        interfaces = (relay.Node, )


class DeviceInput(graphene.InputObjectType, DeviceAttribute):
    """Arguments to create device."""
    pass


class CreateDevice(graphene.Mutation):
    """Mutation to create a device."""
    _device = graphene.Field(
        lambda: Device, description="Device created by this mutation.")

    class Arguments:
        input = DeviceInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['ts_created'] = datetime.utcnow()
        data['ts_modified'] = datetime.utcnow()
        

        _device = DeviceModel(**data)
        db_session.add(_device)
        db_session.commit()

        return CreateDevice(_device=_device)

class UpdateDeviceInput(graphene.InputObjectType, DeviceAttribute):

    _device = graphene.ID(required=True, description="Unique identifier of the Device")

class UpdateDevice(graphene.Mutation):
    _device = graphene.Field(lambda: Device, description="Device updated by this mutation.")

    class Arguments:
        input = UpdateDeviceInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['ts_modified'] = datetime.utcnow()

        _device = db_session.query(DeviceModel).filter_by(id=data['id'])
        _device.update(data)
        db_session.commit()
        _device = db_session.query(DeviceModel).filter_by(id=data['id']).first()

        return UpdateDevice(_device=_device)

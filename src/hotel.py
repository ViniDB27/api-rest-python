from flask_restful import Resource, reqparse
from model.hotel import HotelModel

hoteis = [
    {
        'hotel_id':'alpha',
        'name':'alpha hotel',
        'estrelas':4.3,
        'diaria':420.10
    },
    {
        'hotel_id':'alpha-2',
        'name':'alpha hotel',
        'estrelas':4.3,
        'diaria':420.10
    },
    {
        'hotel_id':'alpha-3',
        'name':'alpha hotel',
        'estrelas':4.3,
        'diaria':420.10
    }
]

class Hoteis(Resource):
    def get(self):
        return hoteis

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')


    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        else:
            return {'message':'hotel not found'}, 404

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message':'hotel {} alread exist'.format(hotel_id)}, 400
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json()

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()        
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.update_hotel(**dados)
            hotel.save_hotel()
            return hotel.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {'message':'hotel {} deleted'.format(hotel_id)}
        return {'message':'hotel not found'}
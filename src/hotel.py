from flask_restful import Resource, reqparse

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


class HotelModel:
    def __init__(self, hotel_id, name, estrelas, diaria):
        self.hotel_id = hotel_id
        self.name = name
        self.estrelas = estrelas
        self.diaria = diaria



class Hoteis(Resource):
    def get(self):
        return hoteis

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel 
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        else:
            return {'message':'hotel not found'}, 404

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel = {
            'hotel_id': hotel_id,
            'name': dados['name'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria']
        }

        hoteis.append(novo_hotel)
        return novo_hotel

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel = {'hotel_id': hotel_id, **dados}
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message':'hotel deleted'}
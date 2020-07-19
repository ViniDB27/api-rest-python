from sql_alchemy import banco


class HotelModel(banco.Model):

    __tablename__ = 'hoteis'

    hotel_id = banco.Column(banco.String, primary_key=True)
    name = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))

    def __init__(self, hotel_id, name, estrelas, diaria):
        self.hotel_id = hotel_id
        self.name = name
        self.estrelas = estrelas
        self.diaria = diaria

    def json(self):
        return{
            'hotel_id':self.hotel_id,
            'name':self.name,
            'estrelas':self.estrelas,
            'diaria':self.diaria
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()

    def update_hotel(self, name, estrelas, diaria):
        self.name = name
        self.estrelas = estrelas
        self.diaria = diaria
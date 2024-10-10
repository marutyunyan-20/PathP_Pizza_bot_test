import uuid
import yookassa
from yookassa import Configuration, Payment


from app.handlers.admin_private import AddProduct


def create_payment_link(amount: int, chat_id):
	id_key = str(uuid.uuid4())
	payment = Payment.create({
		"amount": {
			"value": AddProduct.price,
        	"currency": "RUB"
			},
		"confirmation": {
			"type": "redirect",
        	"return_url": "https://t.me/PathP_Pizza_bot"
			},
			"capture": True,
			"metadata": {
				"chat_id": chat_id
			},
			"description": {
				f'Описание товара: {AddProduct.description}'
			}
}, id_key)

	return payment.confirmation.confirmation_url, payment.id
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton






btnMain = KeyboardButton("Main Menu")

# --- Main Menu --------------------------------

btnSale = KeyboardButton("Sales")
btnReten = KeyboardButton("Retention")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSale, btnReten)

# --- Sales Menu ------------------------------------------

btnRU = KeyboardButton("RU")
btnUZ = KeyboardButton("UZ")
btnEU = KeyboardButton("EU")
SaleMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRU, btnUZ).add(btnMain)

# --- Sales Pack RU ------------------------------------------

btn100 = KeyboardButton('RU/Beginner => 100$')
btn250 = KeyboardButton('RU/Smart Start => 250$')
btn500 = KeyboardButton('RU/Smart Trade => 500$')
salePackMenu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True).add(btn100, btn250, btn500).add(btnMain)

# --- Sales Pack UZ ------------------------------------------

btn100uz = KeyboardButton('UZ/Beginner => 100$')
btn250uz = KeyboardButton('UZ/Smart Start => 250$')
btn500uz = KeyboardButton('UZ/Smart Trade => 500$')
salePackMenuUz = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True).add(btn100uz, btn250uz, btn500uz).add(btnMain)


# --- Reten Menu ------------------------------------------

btnEBanking = KeyboardButton("Internet Banking")
btnEMoney = KeyboardButton("Internet Payments")
btnMTransfers = KeyboardButton("Money Transfer")
btnCash = KeyboardButton("Cash")
btnCrypto = KeyboardButton("Cryptocurrency")
btnOther = KeyboardButton("Other Menu")
retenMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnEBanking,
                                                         btnEMoney,
                                                         btnMTransfers,
                                                         btnCrypto,
                                                         btnCash
                                                         ).add(btnMain)

# --- Other Menu --------------------------------

btnInfo = KeyboardButton("Info Button")
btnMoney = KeyboardButton("Money Button")
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney).add(btnMain)


# --- E Banking Menu --------------------------------

btnSber = KeyboardButton("Sberbank")
btnAlfa = KeyboardButton("Alfa Bank")
btnTinkof = KeyboardButton("Tinkoff Bank")
btnVTB = KeyboardButton("VTB Bank")
btnKaspi = KeyboardButton("Kaspi Bank")
btnMIRCard = KeyboardButton("MIR Card")
EBankingMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSber,
                                                             btnAlfa,
                                                             btnTinkof,
                                                             btnVTB,
                                                             btnKaspi,
                                                             btnMIRCard,
                                                             ).add(btnMain)

# --- Enternet Payments Menu --------------------------------

btnQiwi = KeyboardButton("Qiwi Payments")
btnPayPal = KeyboardButton("PayPal")
btnPayeer = KeyboardButton("Payeer")
btnSkrill = KeyboardButton("Skrill")
EPaymentsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnQiwi,
                                                              btnPayPal,
                                                              btnSkrill,
                                                              btnPayeer
                                                              ).add(btnMain)

# --- Money Transfer Payments Menu --------------------------------

btnWU = KeyboardButton("Western Union")
MTransferMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnWU).add(btnMain)

# --- Cryptocurrency Menu --------------------------------

btnBtc = KeyboardButton("Bitcoin")
btnEth = KeyboardButton("Ethereum")
btnLtc = KeyboardButton("Litecoin")
btnTrc20 = KeyboardButton("TRC20")
btnSol = KeyboardButton("Solana")
CryptoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBtc,
                                                           btnEth,
                                                           btnLtc,
                                                           btnTrc20,
                                                           btnSol
                                                           ).add(btnMain)










btnBitcoin = InlineKeyboardButton(text="Bitcoin", callback_data="cc_bitcoin")
btnLitecoin = InlineKeyboardButton(text="Litecoin", callback_data="cc_litecoin")
btnDogecoin = InlineKeyboardButton(text="Dogecoin", callback_data="cc_dogecoin")

crypto_list = InlineKeyboardMarkup(row_width=1)
crypto_list.insert(btnBitcoin)
crypto_list.insert(btnLitecoin)
crypto_list.insert(btnDogecoin)


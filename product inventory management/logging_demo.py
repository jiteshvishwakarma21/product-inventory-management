import logging

logging.basicConfig(
    filename="inventory.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger(__name__)


def process_product(product_name, price, quantity, stock):

    logger.info("Processing product: %s", product_name)

    if price <= 0:
        logger.error("Invalid product price: %s", price)
        return False

    if quantity <= 0:
        logger.error("Invalid quantity: %s", quantity)
        return False

    logger.debug("Checking available stock")

    if quantity > stock:
        logger.warning("Insufficient stock for %s", product_name)
        return False

    total = price * quantity

    logger.info("Product processed successfully")
    logger.info("Total price: %s", total)

    return True


process_product("Laptop", 50000, 2, 10)
process_product("Mouse", 500, 15, 5)
process_product("Keyboard", -100, 2, 10)

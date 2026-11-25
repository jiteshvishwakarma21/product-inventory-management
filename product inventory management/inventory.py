import logging

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def calculate_total_price(price, quantity):
    """Calculate the total price of products."""

    if price < 0:
        logger.error("Price cannot be negative")
        raise ValueError("Price cannot be negative")

    if quantity <= 0:
        logger.error("Quantity must be greater than zero")
        raise ValueError("Quantity must be greater than zero")

    total = price * quantity

    logger.info("Total price calculated successfully: %s", total)

    return total


def apply_discount(total, discount_percent):
    """Apply discount to the total price."""

    if total < 0:
        logger.error("Total cannot be negative")
        raise ValueError("Total cannot be negative")

    if not 0 <= discount_percent <= 100:
        logger.error("Invalid discount percentage")
        raise ValueError("Discount must be between 0 and 100")

    discount_amount = total * discount_percent / 100

    final_amount = total - discount_amount

    logger.info("Discount applied successfully: %s", final_amount)

    return final_amount


def check_stock(available_stock, requested_quantity):
    """Check whether the requested quantity is available."""

    if available_stock < 0:
        logger.error("Available stock cannot be negative")
        raise ValueError("Available stock cannot be negative")

    if requested_quantity <= 0:
        logger.error("Requested quantity must be greater than zero")
        raise ValueError("Requested quantity must be greater than zero")

    if requested_quantity <= available_stock:
        logger.info("Stock check successful: Product available")
        return True

    logger.warning("Insufficient stock")

    return False

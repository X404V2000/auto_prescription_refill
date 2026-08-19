# test_logger.py
from syslog import logger, write_toFilesys

def test_logger():
    print("Testing logger...")
    
    # Test all log levels
    logger.log_info("Test info message")
    logger.log_success("Test success message")
    logger.log_warning("Test warning message")
    logger.log_error("Test error message")
    
    # Test validation handlers
    write_toFilesys(1, is_valid=True)
    write_toFilesys(5, is_valid=False)
    
    # Test exception handling
    try:
        raise ValueError("Test exception")
    except Exception as e:
        logger.handle_exception(e)
    
    print("✅ Logger test complete!")
    print("Check syslog.log for entries.")

if __name__ == "__main__":
    test_logger()

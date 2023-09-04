import os,sys

class CustomException(Exception):
    def __init__(self,error_message:Exception,error_details:sys):
        self.error_message = CustomException.get_error_details(error_message=error_message,error_details=error_details)

    @staticmethod
    def get_error_details(error_message:Exception,error_details:sys)->str:
        _,_,exc_tb = error_details.exc_info()

        exception_block_line_number = exc_tb.tb_frame.f_lineno
        try_block_line_number = exc_tb.tb_lineno
        filename = exc_tb.tb_frame.f_code.co_filename

        error_message = f"""
        Error occured in execution of :[{filename}] at try block number: [{try_block_line_number}]
        and execption line number : [{exception_block_line_number}]
        error_message : [{error_message}]
"""
        return error_message
 
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()
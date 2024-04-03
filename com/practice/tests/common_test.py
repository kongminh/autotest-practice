# -*- coding: utf-8 -*-

'''
Common testing
'''

from seleniumbase import BaseCase
from com.practice.test_cases.common_test_cases import CommonTestCases
import logging
from config import Config
import pytest

@pytest.mark.skipif(Config.disable_doing, reason="Config")
class CommonTests(CommonTestCases):

    # @pytest.mark.run(order=100)
    # def test_case01(self):
        
    # @pytest.mark.run(order=100)
    # def test_case01(self):
        # logging.info('Test Case 1: Register User')
        # self.SignUp_LoginTest()
        # self.SignUp_InputNameAndEmailTest()
        # self.SignUp_InputPersonalInforTest()
        # self.DeleteAccTest()

    # @pytest.mark.run(order=100)
    # def test_case02(self):
        # logging.info('Test Case 2: Login User with correct email and password')
        # self.SignUp_LoginTest()
        # self.Login_InputEmailPasswordTest()
        # self.DeleteAccTest()
      
    # @pytest.mark.run(order=100)
    # def test_case03(self):
        # logging.info('Test Case 3: Login User with incorrect email and password')
        # self.SignUp_LoginTest()
        # self.Login_InputEmailPasswordTest()
    
    # @pytest.mark.run(order=100)
    # def test_case04(self):
        # logging.info('Test Case 4: Logout User')
        # self.SignUp_LoginTest()
        # self.Login_InputEmailPasswordTest()
        # self.LogoutTest()

    # @pytest.mark.run(order=100)
    # def test_case05(self):     
        # logging.info('Test Case 5: Register User with existing email')
        # self.SignUp_LoginTest()
        # self.SignUp_InputNameAndEmailTest()
      
    #@pytest.mark.run(order=100)
    # def test_case06(self):
        # logging.info('Test Case 6: Contact Us Form')
        # self.ContactUsTest()

    # @pytest.mark.run(order=100)
    # def test_case07(self):
    #     logging.info('Test Case 7: Verify Test Cases Page')
    #     self.VerifyTestcasePageTest()

    # @pytest.mark.run(order=100)
    # def test_case08(self):  
    #     logging.info('Test Case 8: Verify All Products and product detail page')
    #     self.ViewProductTest()

    # @pytest.mark.run(order=100)
    # def test_case09(self):  
    #     logging.info('Test Case 9: Search Product')
    #     self.SearchProductTest()  

    # @pytest.mark.run(order=100)
    # def test_case10(self):  
    #     logging.info('Test Case 10: Verify Subscription in home page')
    #     self.SubscribeTest()  

    # @pytest.mark.run(order=100)
    # def test_case11(self):  
    #     logging.info('Test Case 11: Verify Subscription in Cart page')
    #     self.SubscribeCartTest()    

    # @pytest.mark.run(order=100)
    # def test_case12(self):  
    #     logging.info('Test Case 12: Add Products in Cart')
    #     self.AddProductInCartTest()         

    # @pytest.mark.run(order=100)
    # def test_case13(self):  
    #     logging.info('Test Case 13: Verify Product quantity in Cart')
    #     self.VerifyProductQuantityInCartTest()      

    # @pytest.mark.run(order=100)
    # def test_case14(self):  
    #     logging.info('Test Case 14: Place Order: Register while Checkout')
    #     self.AddProductInCartTest()    
    #     self.ProceedCheckoutTest()
    #     self.SignUp_InputNameAndEmailTest()
    #     self.SignUp_InputPersonalInforTest()
    #     self.PlaceOrderTest()  
    #     self.DeleteAccTest()

    # @pytest.mark.run(order=100)
    # def test_case15(self):  
    #     logging.info('Test Case 15: Place Order: Register before Checkout')
    #     self.SignUp_LoginTest()
    #     self.SignUp_InputNameAndEmailTest()
    #     self.SignUp_InputPersonalInforTest()
    #     self.AddProductInCartTest()    
    #     self.PlaceOrderTest()  
    #     self.DeleteAccTest()    

    # @pytest.mark.run(order=100)
    # def test_case16(self):  
    #     logging.info('Test Case 16: Place Order: Login before Checkout')
    #     self.SignUp_LoginTest()
    #     self.Login_InputEmailPasswordTest()
    #     self.AddProductInCartTest()    
    #     self.PlaceOrderTest()  
    #     self.DeleteAccTest()       

    # @pytest.mark.run(order=100)
    # def test_case17(self):  
    #     logging.info('Test Case 17: Remove Products From Cart')
    #     self.RemoveProductsFromCartTest()  

    # @pytest.mark.run(order=100)
    # def test_case18(self):  
    #     logging.info('Test Case 18: View Category Products')
    #     self.ViewCategoryProductsTest()

    # @pytest.mark.run(order=100)
    # def test_case19(self):  
    #     logging.info('Test Case 19: View & Cart Brand Products')
    #     self.ViewCartBrandProducts()    

    # @pytest.mark.run(order=100)
    # def test_case20(self):  
    #     logging.info('Test Case 20: Search Products and Verify Cart After Login')
    #     self.SearchProductsVerifyCartAfterLoginTest()            

    # @pytest.mark.run(order=100)
    # def test_case21(self):  
    #     logging.info('Test Case 21: Add review on product')
    #     self.AddReviewOnProductTest()      

    # @pytest.mark.run(order=100)
    # def test_case22(self):  
    #     logging.info('Test Case 22: Add to cart from Recommended items')
    #     self.AddRecommendedItems() 

    # @pytest.mark.run(order=100)
    # def test_case23(self):  
    #     logging.info('Test Case 23: Verify address details in checkout page')
    #     self.SignUp_LoginTest()  
    #     self.SignUp_InputNameAndEmailTest()  
    #     self.SignUp_InputPersonalInforTest() 
    #     self.AddProductInCartTest()
    #     self.PlaceOrderTest()   
    #     self.DeleteAccTest()  

    @pytest.mark.run(order=100)
    def test_case24(self):  
        logging.info('Test Case 24: Download Invoice after purchase order')
        self.AddProductInCartTest()
        self.ProceedCheckoutTest()
        self.SignUp_InputNameAndEmailTest()
        self.SignUp_InputPersonalInforTest()
        self.PlaceOrderTest()
        self.DownloadInvoiceTest()
        self.DeleteAccTest()

    # @pytest.mark.run(order=100)
    # def test_case25(self):  
    #     logging.info('Test Case 25: Verify Scroll Up using Arrow button and Scroll Down functionality')
    #     self.ScrollUpTest()
    
    # @pytest.mark.run(order=100)
    # def test_case26(self):  
    #     logging.info('Test Case 26:  Verify Scroll Up without Arrow button and Scroll Down functionality')
    #     self.ScrollUpTopTest()
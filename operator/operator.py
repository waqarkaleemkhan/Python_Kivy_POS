from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import re

class OperatorWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cart=[] #this is an empty list which will hold all the products we add to out cart
        self.qty=[] # this is an empty list which will hold all the quantity of the products we have added to the cart 
        self.total=0.0

    def update_purchases(self):
        pcode=self.ids.code_input.text
        products_container=self.ids.products
        if pcode=='1234' or pcode=='2345':
            details=BoxLayout(size_hint_y=None,height=30,pos_hint={'top':1})
            products_container.add_widget(details)
            code=Label(text=pcode,size_hint_x=.3,color=(.06,.45,.45,1))
            name=Label(text="product one",size_hint_x=.2,color=(.06,.45,.45,1))
            qty=Label(text="1",size_hint_x=.1,color=(.06,.45,.45,1))
            disc=Label(text="0.00",size_hint_x=.1,color=(.06,.45,.45,1))
            price=Label(text="0.00",size_hint_x=.1,color=(.06,.45,.45,1))
            total=Label(text="0.00",size_hint_x=.2,color=(.06,.45,.45,1))
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)



            #updatng the preview with the products data
            pname="product one"
            if pcode=='2345':
                pname="product two"
            pprice=1.00
            self.total+=pprice
            purchase_total='`\n\nTotal\t\t\t\t\t\t\t\t'+str(self.total)
            self.ids.cur_product.text=pname
            self.ids.cur_price.text=str(pprice)
            pqty=str(1)
            preview=self.ids.receipt_preview
            prev_text=preview.text
            _prev=prev_text.find('`')
            if _prev>0:
                prev_text=prev_text[:_prev]
            
            ptarget=-1
            for i,c in enumerate(self.cart):
                if c==pcode: # if the code is already avalible in pcode add the product to the index i of that code
                    ptarget=i 
            if ptarget>=0:
                pqty=self.qty[ptarget]+1
                self.qty[ptarget]=pqty
                expr='%s\t\tx\d\t'%(pname)
                rexpr=pname+'\t\tx'+str(pqty)+'\t'
                nu_text = re.sub(expr,rexpr,prev_text) # re use for regular expression to subtitute these expression for adding the quantity
                preview.text=nu_text+purchase_total
            else:
                self.cart.append(pcode)
                self.qty.append(1)
                nu_preview='\n'.join([prev_text,pname+'\t\tx'+pqty+'\t\t'+str(pprice),purchase_total])
                preview.text=nu_preview

class OperatorApp(App):
    def build(self):
        return OperatorWindow()


if __name__ == "__main__":
    oa = OperatorApp() 
    oa.run() 
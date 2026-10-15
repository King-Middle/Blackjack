import random
import time
import json
p=10000
def save_data(p):
  with open('p.json','w') as f:
    json.dump({"p":p}, f)

def load_data():
  with open('p.json', 'r') as f:
    data = json.load(f)
    if data["p"] == 0:
      data["p"]=10000
      
    return data["p"]
  
print(load_data())
while p>0:
    p=load_data()
    cards=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10]*4
    cards_again=cards

    x=random.choice(cards)
    
    cards.remove(x)
    if len(cards) == 0:
      cards=cards_again
    if x == 1:
      x=11

    y=random.choice(cards)
    cards.remove(y)
    if len(cards) == 0:
      cards=cards_again
    if y == 1:
      y=11

    z=random.choice(cards)
    cards.remove(z)
    if len(cards) == 0:
      cards=cards_again
    if z == 1:
      z=11

    b=random.choice(cards)
    cards.remove(b)
    if len(cards) == 0:
      cards=cards_again
    if b == 1:
      b=11

#*****************************************************************************************************************************************************

    while True:
        try:
            m=int(input("Miktar:"))
            break
        except:
            pass

    if p < m and m < 0:
      continue

#*****************************************************************************************************************************************************

    def system(p,cards,cards_again,x,y,z,b):
      if m*2 <= p:
        c=input("hit / stand / double down / give up\n")
      elif m*2 > p:
        c=input("hit / stand / give up\n")
      if c != "h" and c != "s" and c != "g" and c != "d":
        p=p-m
        
      if c == "h":
        q=random.choice(cards)
        cards.remove(q)
        if len(cards) == 0:
          cards=cards_again
        if q == 1:
          q=11
        time.sleep(1)
        if z == 11:
          if z+b+q > 21:
            z=1
        if b == 11:
          if z+b+q > 21:
            b=1
        if q == 11:
          if z+b+q > 21:
            q=1
        print(z,",",b,",",q)
        if z+b+q > 21:
          p=p-m
          print("Bust")
          
        if z+b+q == 21:
          if x == 11:
            if x+y > 21:
              x=1
          if y == 11:
            if x+y > 21:
              y=1
          time.sleep(1.5)
          print(x,",",y)
          if 17 > x+y:
            r=random.choice(cards)
            cards.remove(r)
            if len(cards) == 0:
              cards=cards_again
            if r == 1:
              r=11
            if x == 11:
              if x+y+r > 21:
                x=1
            if y == 11:
              if x+y+r > 21:
                y=1
            if r == 11:
              if x+y+r > 21:
                r=1
            time.sleep(1.5)
            print(x,",",y,",",r)
            if 17 > x+y+r:
              t=random.choice(cards)
              cards.remove(t)
              if len(cards) == 0:
                cards=cards_again
              if t == 1:
                t=11
              if x == 11:
                if x+y+r+t > 21:
                  x=1
              if y == 11:
                if x+y+r+t > 21:
                  y=1
              if r == 11:
                if x+y+r+t > 21:
                  r=1
              if t == 11:
                if x+y+r+t > 21:
                  t=11
              time.sleep(1.5)
              print(x,",",y,",",r,",",t)
              if 17 > t+r+y+x:
                a=random.choice(cards)
                cards.remove(a)
                if len(cards) == 0:
                  cards=cards_again
                if a == 1:
                  a=11
                if x == 11:
                  if x+y+r+t+a > 21:
                    x=1
                if y == 11:
                  if x+y+r+t+a > 21:
                    y=1
                if r == 11:
                  if x+y+r+t+a > 21:
                    r=1
                if t == 11:
                  if x+y+r+t+a > 21:
                    t=1
                if a == 11:
                  if x+y+r+t+a > 21:
                    a=1
                time.sleep(1.5)
                print(x,",",y,",",r,",",t,",",a)
                if 17 > a+t+r+y+x:
                  u=random.choice(cards)
                  cards.remove(u)
                  if len(cards) == 0:
                    cards=cards_again
                  if u == 1:
                    u=11
                  if x == 11:
                    if x+y+r+t+a+u > 21:
                      x=1
                  if y == 11:
                    if x+y+r+t+a+u > 21:
                      y=1
                  if r == 11:
                    if x+y+r+t+a+u > 21:
                      r=1
                  if t == 11:
                    if x+y+r+t+a+u > 21:
                      t=1
                  if a == 11:
                    if x+y+r+t+a+u > 21:
                      a=1
                  if u == 11:
                    if x+y+r+t+a+u > 21:
                      u=1
                  time.sleep(1.5)
                  print(x,",",y,",",r,",",t,",",a,",",u)
                  if 21>=x+y+r+t+a+u > z+b+q:
                      time.sleep(1)
                      print("Lose")
                      time.sleep(1)
                      p=p-m
                      
                  elif 21>=x+y+r+t+a+u == z+b+q:
                      time.sleep(1)
                      print("Draw")
                      time.sleep(1)
                      
                  else:
                      p=p+m
                      time.sleep(1)
                      print("Win")
                      
                elif 21>=x+y+r+t+a > z+b+q:
                  time.sleep(1)
                  print("Lose")
                  time.sleep(1)
                  p=p-m
                  
                elif 21>=x+y+r+t+a == z+b+q:
                  time.sleep(1)
                  print("Draw")
                  time.sleep(1)
                  
                else:
                  p=p+m
                  time.sleep(1)
                  print("Win")
                  
              elif 21>=x+y+r+t > z+b+q:
                time.sleep(1)
                print("Lose")
                time.sleep(1)
                p=p-m
                
              elif 21>=x+y+r+t == z+b+q:
                time.sleep(1)
                print("Draw")
                time.sleep(1)
                
              else:
                p=p+m
                time.sleep(1)
                print("Win")
                time.sleep(1)
                
            elif 21>=x+y+r > z+b+q:
              time.sleep(1)
              print("Lose")
              time.sleep(1)
              p=p-m
              
            elif 21>=x+y+r == z+b+q:
              time.sleep(1)
              print("Draw")
              time.sleep(1)
              
            else:
              p=p+m
              time.sleep(1)
              print("Win")
              time.sleep(1)
              
          elif 21>=x+y > z+b+q:
            time.sleep(1)
            print("Lose")
            time.sleep(1)
            p=p-m
            
          elif 21>=x+y == z+b+q:
            time.sleep(1)
            print("Draw")
            time.sleep(1)
            
          else:
            p=p+m
            time.sleep(1)
            print("Win")
            time.sleep(1)
            

        elif z+b+q < 21:
          c1=input("hit / stand\n")
          if c1 != "h" and c1 != "s":
            p=p-m
            
          if c1 == "h":
            w=random.choice(cards)
            cards.remove(w)
            if len(cards) == 0:
              cards=cards_again
            if w == 1:
              w=11
            time.sleep(1)
            if z == 11:
              if z+b+q+w > 21:
                z=1
            if b == 11:
              if z+b+q+w > 21:
                b=1
            if q == 11:
              if z+b+q+w > 21:
                q=1
            if w == 11:
              if z+b+q+w > 21:
                w=1
            print(z,",",b,",",q,",",w)
            if z+b+q+w > 21:
              p=p-m
              print("Bust")
              
            elif z+b+q+w == 21:
              if 17 > x+y:
                if x == 11:
                  if x+y > 21:
                    x=1
                if y == 11:
                  if x+y > 21:
                    y=1
                time.sleep(1.5)
                print(x,",",y)
              if 17 > x+y:
                r=random.choice(cards)
                cards.remove(r)
                if len(cards) == 0:
                  cards=cards_again
                if r == 1:
                  r=11
                if x == 11:
                  if x+y+r > 21:
                    x=1
                if y == 11:
                  if x+y+r > 21:
                    y=1
                if r == 11:
                  if x+y+r > 21:
                    r=1
                time.sleep(1.5)
                print(x,",",y,",",r)
                if 17 > x+y+r:
                  t=random.choice(cards)
                  cards.remove(t)
                  if len(cards) == 0:
                    cards=cards_again
                  if t == 1:
                    t=11
                  if x == 11:
                    if x+y+r+t > 21:
                      x=1
                  if y == 11:
                    if x+y+r+t > 21:
                      y=1
                  if r == 11:
                    if x+y+r+t > 21:
                      r=1
                  if t == 11:
                    if x+y+r+t > 21:
                      t=1
                  time.sleep(1.5)
                  print(x,",",y,",",r,",",t)
                  if 17 > t+r+y+x:
                    a=random.choice(cards)
                    cards.remove(a)
                    if len(cards) == 0:
                      cards=cards_again
                    if a == 1:
                      a=11
                    if x == 11:
                      if x+y+r+t+a > 21:
                        x=1
                    if y == 11:
                      if x+y+r+t+a > 21:
                        y=1
                    if r == 11:
                      if x+y+r+t+a > 21:
                        r=1
                    if t == 11:
                      if x+y+r+t+a > 21:
                        t=1
                    if a == 11:
                      if x+y+r+t+a > 21:
                        a=1
                    time.sleep(1.5)
                    print(x,",",y,",",r,",",t,",",a)
                    if 17 > a+t+r+y+x:
                      u=random.choice(cards)
                      cards.remove(u)
                      if len(cards) == 0:
                        cards=cards_again
                      if u == 1:
                        u=11
                      if x == 11:
                        if x+y+r+t+a+u > 21:
                          x=1
                      if y == 11:
                        if x+y+r+t+a+u > 21:
                          y=1
                      if r == 11:
                        if x+y+r+t+a+u > 21:
                          r=1
                      if t == 11:
                        if x+y+r+t+a+u > 21:
                          t=1
                      if a == 11:
                        if x+y+r+t+a+u > 21:
                          a=1
                      if u == 11:
                        if x+y+r+t+a+u > 21:
                          u=1
                      time.sleep(1.5)
                      print(x,",",y,",",r,",",t,",",a,",",u)
                      if 21>=x+y+r+t+a+u > z+b+q:
                          time.sleep(1)
                          print("Lose")
                          time.sleep(1)
                          p=p-m
                          
                      elif 21>=x+y+r+t+a+u == z+b+q:
                          time.sleep(1)
                          print("Draw")
                          time.sleep(1)
                          
                      else:
                          p=p+m
                          time.sleep(1)
                          print("Win")
                          time.sleep(1)
                          
                    elif 21>=y+t+r+a+x > z+b+q+w:
                      time.sleep(1)
                      print("Lose")
                      time.sleep(1)
                      p=p-m
                      
                    elif 21>=y+t+r+a+x == z+b+q+w:
                      time.sleep(1)
                      print("Draw")
                      time.sleep(1)
                      p=p
                      
                    else:
                      p=p+m
                      time.sleep(1)
                      print("Win")
                      time.sleep(1)
                      
                  elif 21>=t+r+y+x > z+b+q+w:
                    time.sleep(1)
                    print("Lose")
                    time.sleep(1)
                    p=p-m
                    
                  elif 21>=t+r+y+x == z+b+q+w:
                    time.sleep(1)
                    print("Draw")
                    time.sleep(1)
                    
                  else:
                    p=p+m
                    time.sleep(1)
                    print("Win")
                    time.sleep(1)
                    
                elif 21>=r+y+x > z+b+q+w:
                  time.sleep(1)
                  print("Lose")
                  time.sleep(1)
                  p=p-m
                  
                elif 21>=r+y+x == z+b+q+w:
                  time.sleep(1)
                  print("Draw")
                  time.sleep(1)
                  
                else:
                  p=p+m
                  time.sleep(1)
                  print("Win")
                  time.sleep(1)
                  
              elif 21>=y+x > z+b+q+w:
                time.sleep(1)
                print("Lose")
                time.sleep(1)
                p=p-m
                
              elif 21>=y+x == z+b+q+w:
                time.sleep(1)
                print("Draw")
                time.sleep(1)
                
              else:
                p=p+m
                time.sleep(1)
                print("Win")
                time.sleep(1)
                
            elif z+b+q+w < 21:
              c2=input("hit / stand\n")
              if c2 != "h" and c2 != "s":
                p=p-m
                
              if c2 == "h":
                e=random.choice(cards)
                cards.remove(e)
                if len(cards) == 0:
                  cards=cards_again
                if e == 1:
                  e=11
                time.sleep(1)
                if z == 11:
                  if z+b+q+w+e > 21:
                    z=1
                if b == 11:
                  if z+b+q+w+e > 21:
                    b=1
                if q == 11:
                  if z+b+q+w+e > 21:
                    q=1
                if w == 11:
                  if z+b+q+w+e > 21:
                    w=1
                if e == 11:
                  if z+b+q+w+e > 21:
                    e=1
                print(z,",",b,",",q,",",w,",",e)
                if z+b+q+w+e > 21:
                  p=p-m
                  print("Bust")
                  
                else:
                  p=p+m
                  
              elif c2 == "s":
                time.sleep(1)
                if x == 11:
                  if x+y > 21:
                    x=1
                if y == 11:
                  if x+y > 21:
                    y=1
                print(x,",",y)
                if 17 > x+y:
                  r=random.choice(cards)
                  cards.remove(r)
                  if len(cards) == 0:
                    cards=cards_again
                  if r == 1:
                    r=11
                  time.sleep(1.5)
                  if x == 11:
                    if x+y+r > 21:
                      x=1
                  if y == 11:
                    if x+y+r > 21:
                      y=1
                  if r == 11:
                    if x+y+r > 21:
                      r=1
                  print(x,",",y,",",r)
                  if 17 > x+y+r:
                    t=random.choice(cards)
                    cards.remove(t)
                    if len(cards) == 0:
                      cards=cards_again
                    if t == 1:
                      t=11
                    time.sleep(1.5)
                    if x == 11:
                      if x+y+r+t > 21:
                        x=1
                    if y == 11:
                      if x+y+r+t > 21:
                        y=1
                    if r == 11:
                      if x+y+r+t > 21:
                        r=1
                    if t == 11:
                      if x+y+r+t > 21:
                        t=1
                    print(x,",",y,",",r,",",t)
                    if 17 > t+r+y+x:
                      a=random.choice(cards)
                      cards.remove(a)
                      if len(cards) == 0:
                        cards=cards_again
                      if a == 1:
                        a=11
                      time.sleep(1.5)
                      if x == 11:
                        if x+y+r+t+a > 21:
                          x=1
                      if y == 11:
                        if x+y+r+t+a > 21:
                          y=1
                      if r == 11:
                        if x+y+r+t+a > 21:
                          r=1
                      if t == 11:
                        if x+y+r+t+a > 21:
                          t=1
                      if a == 11:
                        if x+y+r+t+a > 21:
                          a=1
                      print(x,",",y,",",r,",",t,",",a)
                      if 17 > a+t+r+y+x:
                        u=random.choice(cards)
                        cards.remove(u)
                        if len(cards) == 0:
                          cards=cards_again
                        if u == 1:
                          u=11
                        time.sleep(1.5)
                        if x == 11:
                          if x+y+r+t+a+u > 21:
                            x=1
                        if y == 11:
                          if x+y+r+t+a+u > 21:
                            y=1
                        if r == 11:
                          if x+y+r+t+a+u > 21:
                            r=1
                        if t == 11:
                          if x+y+r+t+a+u > 21:
                            t=1
                        if a == 11:
                          if x+y+r+t+a+u > 21:
                            a=1
                        if u == 11:
                          if x+y+r+t+a+u > 21:
                            u=1
                        print(x,",",y,",",r,",",t,",",a,",",u)
                        if 21>=x+y+r+t+a+u:
                            time.sleep(1)
                            print("Lose")
                            time.sleep(1)
                            p=p-m
                            
                        elif 21>=x+y+r+t+a+u == z+b+q:
                            time.sleep(1)
                            print("Draw")
                            time.sleep(1)
                            
                        else:
                            p=p+m
                            time.sleep(1)
                            print("Win")
                            
                      elif 21>=y+t+r+a+x > z+b+q+w:
                        time.sleep(1)
                        print("Lose")
                        time.sleep(1)
                        p=p-m
                        
                      elif 21>=y+t+r+a+x == z+b+q+w:
                        time.sleep(1)
                        print("Draw")
                        time.sleep(1)
                        
                      else:
                        p=p+m
                        time.sleep(1)
                        print("Win")
                        time.sleep(1)
                        
                    elif 21>=t+r+y+x > z+b+q+w:
                      time.sleep(1)
                      print("Lose")
                      time.sleep(1)
                      p=p-m
                      
                    elif 21>=t+r+y+x == z+b+q+w:
                      time.sleep(1)
                      print("Draw")
                      time.sleep(1)
                      
                    else:
                      p=p+m
                      time.sleep(1)
                      print("Win")
                      time.sleep(1)
                      
                  elif 21>=r+y+x > z+b+q+w:
                    time.sleep(1)
                    print("Lose")
                    time.sleep(1)
                    p=p-m
                    
                  elif 21>=r+y+x == z+b+q+w:
                    time.sleep(1)
                    print("Draw")
                    time.sleep(1)
                    
                  else:
                    p=p+m
                    time.sleep(1)
                    print("Win")
                    time.sleep(1)
                    
                elif 21>=y+x > z+b+q+w:
                  time.sleep(1)
                  print("Lose")
                  time.sleep(1)
                  p=p-m
                  
                elif 21>=y+x == z+b+q+w:
                  time.sleep(1)
                  print("Draw")
                  time.sleep(1)
                  
                else:
                  p=p+m
                  time.sleep(1)
                  print("Win")
                  time.sleep(1)
                  
          elif c1 == "s":
              time.sleep(1)
              if x == 11:
                if x+y > 21:
                  x=1
              if y == 11:
                if x+y > 21:
                  y=1
              print(x,",",y)
              if 17 > x+y:
                r=random.choice(cards)
                cards.remove(r)
                if len(cards) == 0:
                  cards=cards_again
                if r == 1:
                  r=11
                time.sleep(1.5)
                if x == 11:
                  if x+y+r > 21:
                    x=1
                if y == 11:
                  if x+y+r > 21:
                    y=1
                if r == 11:
                  if x+y+r > 21:
                    r=1
                print(x,",",y,",",r)
                if 17 > x+y+r:
                  t=random.choice(cards)
                  cards.remove(t)
                  if len(cards) == 0:
                    cards=cards_again
                  if t == 1:
                    t=11
                  time.sleep(1.5)
                  if x == 11:
                    if x+y+r+t > 21:
                      x=1
                  if y == 11:
                    if x+y+r+t > 21:
                      y=1
                  if r == 11:
                    if x+y+r+t > 21:
                      r=1
                  if t == 11:
                    if x+y+r+t > 21:
                      t=1
                  print(x,",",y,",",r,",",t)
                  if 17 > t+r+y+x:
                    a=random.choice(cards)
                    cards.remove(a)
                    if len(cards) == 0:
                      cards=cards_again
                    if a == 1:
                      a=11
                    time.sleep(1.5)
                    if x == 11:
                      if x+y+r+t+a > 21:
                        x=1
                    if y == 11:
                      if x+y+r+t+a > 21:
                        y=1
                    if r == 11:
                      if x+y+r+t+a > 21:
                        r=1
                    if t == 11:
                      if x+y+r+t+a > 21:
                        t=1
                    if a == 11:
                      if x+y+r+t+a > 21:
                        a=1
                    print(x,",",y,",",r,",",t,",",a)
                    if 17 > a+t+r+y+x:
                      u=random.choice(cards)
                      cards.remove(u)
                      if len(cards) == 0:
                        cards=cards_again
                      if u == 1:
                        u=11
                      time.sleep(1.5)
                      if x == 11:
                        if x+y+r+t+a+u > 21:
                          x=1
                      if y == 11:
                        if x+y+r+t+a+u > 21:
                          y=1
                      if r == 11:
                        if x+y+r+t+a+u > 21:
                          r=1
                      if t == 11:
                        if x+y+r+t+a+u > 21:
                          t=1
                      if a == 11:
                        if x+y+r+t+a+u > 21:
                          a=1
                      if u == 11:
                        if x+y+r+t+a+u > 21:
                          u=1
                      print(x,",",y,",",r,",",t,",",a,",",u)
                      if 21>=x+y+r+t+a+u > z+b+q:
                          time.sleep(1)
                          print("Lose")
                          time.sleep(1)
                          p=p-m
                          
                      elif 21>=x+y+r+t+a+u == z+b+q:
                          time.sleep(1)
                          print("Draw")
                          time.sleep(1)
                          
                      else:
                          p=p+m
                          time.sleep(1)
                          print("Win")
                          time.sleep(1)
                          
                    elif 21>=y+t+r+a+x > z+b+q:
                      time.sleep(1)
                      print("Lose")
                      time.sleep(1)
                      p=p-m
                      
                    elif 21>=y+t+r+a+x == z+b+q:
                      time.sleep(1)
                      print("Draw")
                      time.sleep(1)
                      
                    else:
                      p=p+m
                      time.sleep(1)
                      print("Win")
                      time.sleep(1)
                      
                  elif 21>=t+r+y+x > z+b+q:
                    time.sleep(1)
                    print("Lose")
                    time.sleep(1)
                    p=p-m
                    
                  elif 21>=t+r+y+x == z+b+q:
                    time.sleep(1)
                    print("Draw")
                    time.sleep(1)
                    
                  else:
                    p=p+m
                    time.sleep(1)
                    print("Win")
                    time.sleep(1)
                    
                elif 21>=r+y+x > z+b+q:
                  time.sleep(1)
                  print("Lose")
                  time.sleep(1)
                  p=p-m
                  
                elif 21>=r+y+x == z+b+q:
                  time.sleep(1)
                  print("Draw")
                  time.sleep(1)
                  
                else:
                  p=p+m
                  time.sleep(1)
                  print("Win")
                  time.sleep(1)
                  
              elif 21>=y+x > z+b+q:
                time.sleep(1)
                print("Lose")
                time.sleep(1)
                p=p-m
                
              elif 21>=y+x == z+b+q:
                time.sleep(1)
                print("Draw")
                time.sleep(1)
                
              else:
                p=p+m
                time.sleep(1)
                print("Win")
                time.sleep(1)
                
      elif c == "s":
        time.sleep(1)
        if z+b > 21:
          p=p-m
          print("Bust")
          
        if x == 11:
          if x+y > 21:
            x=1
        if y == 11:
          if x+y > 21:
            y=1
        print(x,",",y)
        if 17 > x+y:
          r=random.choice(cards)
          cards.remove(r)
          if len(cards) == 0:
            cards=cards_again
          if r == 1:
            r=11
          time.sleep(1.5)
          if x == 11:
            if x+y+r > 21:
              x=1
          if y == 11:
            if x+y+r > 21:
              y=1
          if r == 11:
            if x+y+r > 21:
              r=1
          print(x,",",y,",",r)
          if 17 > x+y+r:
            t=random.choice(cards)
            cards.remove(t)
            if len(cards) == 0:
              cards=cards_again
            if t == 1:
              t=11
            time.sleep(1.5)
            if x == 11:
              if x+y+r+t > 21:
                x=1
            if y == 11:
              if x+y+r+t > 21:
                y=1
            if r == 11:
              if x+y+r+t > 21:
                r=1
            if t == 11:
              if x+y+r+t > 21:
                t=1
            print(x,",",y,",",r,",",t)
            if 17 > t+r+y+x:
              a=random.choice(cards)
              cards.remove(a)
              if len(cards) == 0:
                cards=cards_again
              if a == 1:
                a=11
              time.sleep(1.5)
              if x == 11:
                if x+y+r+t+a > 21:
                  x=1
              if y == 11:
                if x+y+r+t+a > 21:
                  y=1
              if r == 11:
                if x+y+r+t+a > 21:
                  r=1
              if t == 11:
                if x+y+r+t+a > 21:
                  t=1
              if a == 11:
                if x+y+r+t+a > 21:
                  a=1
              print(x,",",y,",",r,",",t,",",a)
              if 17 > a+t+r+y+x:
                u=random.choice(cards)
                cards.remove(u)
                if len(cards) == 0:
                  cards=cards_again
                if u == 1:
                  u=11
                time.sleep(1.5)
                if x == 11:
                  if x+y+r+t+a+u > 21:
                    x=1
                if y == 11:
                  if x+y+r+t+a+u > 21:
                    y=1
                if r == 11:
                  if x+y+r+t+a+u > 21:
                    r=1
                if t == 11:
                  if x+y+r+t+a+u > 21:
                    t=1
                if a == 11:
                  if x+y+r+t+a+u > 21:
                    a=1
                if u == 11:
                  if x+y+r+t+a+u > 21:
                    u=1
                print(x,",",y,",",r,",",t,",",a,",",u)
                if 21>=x+y+r+t+a+u > z+b:
                    time.sleep(1)
                    print("Lose")
                    time.sleep(1)
                    p=p-m
                    
                elif 21>=x+y+r+t+a+u == z+b:
                    time.sleep(1)
                    print("Draw")
                    time.sleep(1)
                    
                else:
                    p=p+m
                    time.sleep(1)
                    print("Win")
                    
              elif 21>=y+t+r+a+x > z+b:
                time.sleep(1)
                print("Lose")
                time.sleep(1)
                p=p-m
                
              elif 21>=y+t+r+a+x == z+b:
                time.sleep(1)
                print("Draw")
                time.sleep(1)
                
              else:
                p=p+m
                time.sleep(1)
                print("Win")
                time.sleep(1)
                
            elif 21>=t+r+y+x > z+b:
              time.sleep(1)
              print("Lose")
              time.sleep(1)
              p=p-m
              
            elif 21>=t+r+y+x == z+b:
              time.sleep(1)
              print("Draw")
              time.sleep(1)
              
            else:
              p=p+m
              time.sleep(1)
              print("Win")
              time.sleep(1)
              
          elif 21>=r+y+x > z+b:
            time.sleep(1)
            print("Lose")
            time.sleep(1)
            p=p-m
            
          elif 21>=r+y+x == z+b:
            time.sleep(1)
            print("Draw")
            time.sleep(1)
            
          else:
            p=p+m
            time.sleep(1)
            print("Win")
            time.sleep(1)
            
        elif 21>=y+x > z+b:
          time.sleep(1)
          print("Lose")
          time.sleep(1)
          p=p-m
          
        elif 21>=y+x == z+b:
          time.sleep(1)
          print("Draw")
          time.sleep(1)
          
        else:
          p=p+m
          time.sleep(1)
          print("Win")
          time.sleep(1)
          

      elif c == "d":
        q=random.choice(cards)
        cards.remove(q)
        if len(cards) == 0:
          cards=cards_again
        if q == 1:
          q=11
        time.sleep(1)
        if z == 11:
          if z+b+q > 21:
            z=1
        if b == 11:
          if z+b+q > 21:
            b=1
        if q == 11:
          if z+b+q > 21:
            q=1
        print(z,",",b,",",q)
        if x == 11:
          if x+y > 21:
            x=1
        if y == 11:
          if x+y > 21:
            y=1
        time.sleep(1.5)
        print(x,",",y)
        if z+b+q > 21:
          p=p-m*2
          print("Bust")
          
        elif 17 > x+y:
          r=random.choice(cards)
          cards.remove(r)
          if len(cards) == 0:
            cards=cards_again
          if r == 1:
            r=11
          if x == 11:
            if x+y+r > 21:
              x=1
          if y == 11:
            if x+y+r > 21:
              y=1
          if r == 11:
            if x+y+r > 21:
              r=1
          time.sleep(1.5)
          print(x,",",y,",",r)
          if 17 > x+y+r:
            t=random.choice(cards)
            cards.remove(t)
            if len(cards) == 0:
              cards=cards_again
            if t == 1:
              t=11
            if x == 11:
              if x+y+r+t > 21:
                x=1
            if y == 11:
              if x+y+r+t > 21:
                  y=1
            if r == 11:
              if x+y+r+t > 21:
                  r=1
            if t == 11:
              if x+y+r+t > 21:
                  t=1
            time.sleep(1.5)
            print(x,",",y,",",r,",",t)
            if 17 > t+r+y+x:
              a=random.choice(cards)
              cards.remove(a)
              if len(cards) == 0:
                cards=cards_again
              if a == 1:
                a=11
              if x == 11:
                if x+y+r+t+a > 21:
                  x=1
              if y == 11:
                if x+y+r+t+a > 21:
                  y=1
              if r == 11:
                if x+y+r+t+a > 21:
                  r=1
              if t == 11:
                if x+y+r+t+a > 21:
                  t=1
              if a == 11:
                if x+y+r+t+a > 21:
                  a=1
              time.sleep(1.5)
              print(x,",",y,",",r,",",t,",",a)
              if 17 > a+t+r+y+x:
                u=random.choice(cards)
                cards.remove(u)
                if len(cards) == 0:
                  cards=cards_again
                if u == 1:
                  u=11
                if x == 11:
                  if x+y+r+t+a+u > 21:
                    x=1
                if y == 11:
                  if x+y+r+t+a+u > 21:
                    y=1
                if r == 11:
                  if x+y+r+t+a+u > 21:
                    r=1
                if t == 11:
                  if x+y+r+t+a+u > 21:
                    t=1
                if a == 11:
                  if x+y+r+t+a+u > 21:
                    a=1
                if u == 11:
                  if x+y+r+t+a+u > 21:
                    u=1
                time.sleep(1.5)
                print(x,",",y,",",r,",",t,",",a,",",u)
                if 21>=x+y+r+t+a+u > z+b+q:
                    time.sleep(1)
                    print("Lose")
                    time.sleep(1)
                    p=p-m*2
                    
                elif 21>=x+y+r+t+a+u == z+b+q:
                    time.sleep(1)
                    print("Draw")
                    time.sleep(1)
                    
                else:
                    p=p+m*2
                    time.sleep(1)
                    print("Win")
                    
              elif 21>=x+y+r+t+a > z+b+q:
                time.sleep(1)
                print("Lose")
                time.sleep(1)
                p=p-m*2
                
              elif 21>=x+y+r+t+a == z+b+q:
                time.sleep(1)
                print("Draw")
                time.sleep(1)
                
              else:
                p=p+m*2
                time.sleep(1)
                print("Win")
                time.sleep(1)
                
            elif 21>=x+y+r+t > z+b+q:
              time.sleep(1)
              print("Lose")
              time.sleep(1)
              p=p-m*2
              
            elif 21>=x+y+r+t == z+b+q:
              time.sleep(1)
              print("Draw")
              time.sleep(1)
              
            else:
              p=p+m*2
              time.sleep(1)
              print("Win")
              time.sleep(1)
              
          elif 21>=x+y+r > z+b+q:
            time.sleep(1)
            print("Lose")
            time.sleep(1)
            p=p-m*2
            
          elif 21>=x+y+r == z+b+q:
            time.sleep(1)
            print("Draw")
            
          else:
            p=p+m*2
            time.sleep(1)
            print("Win")
            time.sleep(1)
            
        elif 21>=x+y > z+b+q:
          time.sleep(1)
          print("Lose")
          time.sleep(1)
          p=p-m*2
          
        elif 21>=x+y == z+b+q:
          time.sleep(1)
          print("Draw")
          time.sleep(1)
          
        else:
          p=p+m*2
          time.sleep(1)
          print("Win")
          time.sleep(1)
          
      if c == "g":
        p=p-m//2
        
      save_data(p)
      print(p)

#*****************************************************************************************************************************************************

    if x == 11:
      if x+y > 21:
        x=1
    if y == 11:
      if x+y > 21:
        y=1
    print(x,",","?")
    if z == 11:
      if z+b > 21:
        z=1
    if b == 11:
      if z+b > 21:
        b=1
    print(z,",",b)
    if z+b == 21:
      time.sleep(1)
      p=p+m*3//2
      print("Blackjack")
      time.sleep(1)
      print(p)
      save_data(p)
    else:
      if p/2 >= m and x == 11:
        ic=input("insurance y-n\n")
        time.sleep(1)
        if y == 10:
          if ic == "y":
            print(x,",",y)
            p=p
            
          elif ic == "n":
            p=p-m
          print(p)
        if y != 10:
          if ic == "y":
            p=p-m
          system(p,cards,cards_again,x,y,z,b)
        save_data(p)

#*****************************************************************************************************************************************************

      else:
        system(p,cards,cards_again,x,y,z,b)
        

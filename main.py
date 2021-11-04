import cv2 as cv
import glob



#initializing variables:
dist=0
xlist=[];ylist=[];alist=[]
nb = input("Please enter the number of the model you want from 1 to 3 :")
original_model= cv.imread("modele")
#loading all the images using glob.iglob function:
A=[]
B=[]
C=[]
for f in glob.iglob("image1/*"):
    image1 = cv.imread(f)
    A.append(image1)
for g in glob.iglob("image2/*"):
    image2 = cv.imread(g)
    B.append(image2)
for h in glob.iglob("image3/*"):
    image3 = cv.imread(h)
    C.append(image3)

#the first model
mod1 = cv.imread('modele/1.png')
mod1 = cv.resize(mod1, None, fx= 0.8, fy= 0.8,interpolation=cv.INTER_CUBIC)
mod_gray1 = cv.cvtColor(mod1, cv.COLOR_BGR2GRAY)
mod_blur1 = cv.GaussianBlur(mod_gray1, (3,3),2 )
mod_canny1 = cv.Canny(mod_blur1,10,40)
contour1, _ = cv.findContours(mod_canny1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

#the second model
mod2 = cv.imread('modele/2.png')
mod2 = cv.resize(mod2, None, fx= 0.8, fy= 0.8,interpolation=cv.INTER_CUBIC)
mod_gray2 = cv.cvtColor(mod2, cv.COLOR_BGR2GRAY)
mod_blur2 = cv.GaussianBlur(mod_gray2, (3,3),2 )
mod_canny2 = cv.Canny(mod_blur2,10,40)
contour2, _ = cv.findContours(mod_canny2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

#the third model
mod3 = cv.imread('modele/3.png')
mod3 = cv.resize(mod3, None, fx= 0.8, fy= 0.8,interpolation=cv.INTER_CUBIC)
mod_gray3 = cv.cvtColor(mod3, cv.COLOR_BGR2GRAY)
mod_blur3 = cv.GaussianBlur(mod_gray3, (3,3),2 )
mod_canny3 = cv.Canny(mod_blur3,10,40)
contour3, _ = cv.findContours(mod_canny3, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

#first model treatement
if nb=='1':
    f = open('coordonées_modèle.txt', 'w')
    f.write(f'MODEL N1  : \n')
    f.write(f'Number of forms : {len(contour1)} \n')
    f.close()
    print('MODEL N° 1 : ')
    print("Number of forms :", len(contour1))
    for cnt in contour1:

        cv.drawContours(mod1, contour1, -1, (255, 0, 255), 2)
        area = cv.contourArea(cnt)
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
        x, y, w, h = cv.boundingRect(approx)
        cv.rectangle(mod1, (x, y), (x + w, y + h), (0, 255, 0), 3)
        nb_point = len(approx)
        if nb_point == 3:
            texte_form = 'Tri'
        elif nb_point == 4:
            dist = w / h
            if dist > 0.95 and dist < 1.05:texte_form = 'Carre'
            else:texte_form = 'Rectangle'
        else:texte_form = 'Cercle'
        print(texte_form, ": Largeur=", w, ",Longueur =", h, ",Position X=", x, ",Position Y=", y, ",Surface=", area)
        xlist.append(x)
        ylist.append(y)
        alist.append(area)
        f = open('coordonées_modèle.txt', 'a')
        f.write(f'{texte_form}: Largeur= {w},Longueur= {h},Position X= {x},Position Y= {y},Surface= {area} \n')
        f.close()
    cv.imshow('Contour', mod1)

#second model treatement
elif nb=='2':
    f = open('coordonées_modèle.txt', 'w')
    f.write(f'MODEL N2  : \n')
    f.write(f'Number of forms: {len(contour2)} \n')
    f.close()
    print('MODEL N° 2 : ')
    print("Number of forms :", len(contour2))
    for cont2 in contour2:

        cv.drawContours(mod2, contour2, -1, (255, 0, 255), 2)
        area1 = cv.contourArea(cont2)
        peri1 = cv.arcLength(cont2, True)
        approx1 = cv.approxPolyDP(cont2, 0.02 * peri1, True)
        x1, y1, w1, h1 = cv.boundingRect(approx1)
        cv.rectangle(mod2, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 3)
        nb_point1 = len(approx1)
        if nb_point1 == 3:texte_form1 = 'Tri'
        elif nb_point1 == 4:
            dist1 = w1 / h1
            if dist > 0.95 and dist < 1.05: texte_form1 = 'Carre'
            else: texte_form1 = 'Rectangle'
        else: texte_form1 = 'Cercle'
        print(texte_form1, ": Largeur=", w1, ",Longueur =", h1, ",Position X=", x1, ",Position Y=", y1, ",Surface=", area1)
        xlist.append(x1)
        ylist.append(y1)
        alist.append(area1)
        f = open('coordonées_modèle.txt', 'a')
        f.write(f'{texte_form1}: Largeur= {w1},Longueur= {h1},Position X= {x1},Position Y= {y1},Surface= {area1} \n')
        f.close()
    cv.imshow('Contour2', mod2)

#Third model treatement
elif nb == '3':
    f = open('coordonées_modèle.txt', 'w')
    f.write(f'MODEL N3  : \n')
    f.write(f'Number of forms : {len(contour3)} \n')
    f.close()
    print('MODEL N° 3 : ')
    print("Number of forms :", len(contour3))
    for cont3 in contour3:
        cv.drawContours(mod3, contour3, -1, (255, 0, 255), 2)
        area2 = cv.contourArea(cont3)
        peri2 = cv.arcLength(cont3, True)
        approx2 = cv.approxPolyDP(cont3, 0.02 * peri2, True)
        x2, y2, w2, h2 = cv.boundingRect(approx2)
        cv.rectangle(mod3, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 3)
        nb_point2 = len(approx2)
        if nb_point2 == 3: texte_form2 = 'Tri'
        elif nb_point2 == 4:
            dist = w2 / h2
            if dist > 0.95 and dist < 1.05:texte_form2 = 'Carre'
            else:texte_form2 = 'Rectangle'
        else:texte_form2 = 'Cercle'
        print(texte_form2, ": Largeur=", w2, ",Longueur=", h2, ",Position X=", x2, ",Position Y=", y2, ",Surface=", area2)
        xlist.append(x2)
        ylist.append(y2)
        alist.append(area2)
        f = open('coordonées_modèle.txt', 'a')
        f.write(f'{texte_form2}: Largeur= {w2},Longueur= {h2},Position X= {x2},Position Y= {y2},Surface= {area2} \n')
        f.close()
    cv.imshow('Contour3', mod3)
else :
    print("invalid value")
#Treatement of first model images:

if nb == '1':
    for i in range (0,9):
        xlist1 = [];ylist1 = [];alist1 = []
        A[i] = cv.resize(A[i], None, fx=0.8, fy=0.8, interpolation=cv.INTER_CUBIC)
        img_gray = cv.cvtColor(A[i], cv.COLOR_BGR2GRAY)
        img_blur = cv.GaussianBlur(img_gray, (3, 3), 2)
        img_canny = cv.Canny(img_blur, 10, 40)
        ctr, _ = cv.findContours(img_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        print("-----------------------------------------------------------------")
        print('PIECE N : ',i+1)
        print("Number of peices :", len(ctr))
        for cont1 in ctr:
            cv.drawContours(A[i], ctr, -1, (255, 0, 255), 2)
            area1 = cv.contourArea(cont1)
            peri1 = cv.arcLength(cont1, True)
            approx1 = cv.approxPolyDP(cont1, 0.02 * peri1, True)
            x1, y1, w1, h1 = cv.boundingRect(approx1)
            cv.rectangle(A[i], (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 3)
            nb_point1 = len(approx1)
            if nb_point1 == 3:texte_form1 = 'Tri'
            elif nb_point1 == 4:
                dist1 = w1 / h1
                if dist1 > 0.95 and dist1 < 1.05:texte_form1 = 'Carre'
                else:texte_form1 = 'Rectangle'
            else:texte_form1 = 'Cercle'
            print(texte_form1, ": Largeur=", w1, ",Longueur=", h1, ",Position X=", x1, ",Position Y=", y1,
                  ",Surface=", area1)
            xlist1.append(x1);ylist1.append(y1);alist1.append(area1)
        if xlist==xlist1 and ylist==ylist1 and alist==alist1:
            print("===>  This is a match ")
            cv.imwrite('validated_model\model1 match  N%s.jpg' % (i+1), A[i])


        else :
            print("===>  not a match ")
            cv.imwrite('unvalidated_model\ model1 not a match N%s.jpg' % (i+1), A[i])

#Treatement of second model images:
if nb == '2':
    for i in range (0,10):
        xlist2 = [];ylist2 = [];alist2 = [];ct2=0
        B[i] = cv.resize(B[i], None, fx=0.8, fy=0.8, interpolation=cv.INTER_CUBIC)
        img_gray = cv.cvtColor(B[i], cv.COLOR_BGR2GRAY)
        img_blur = cv.GaussianBlur(img_gray, (3, 3), 2)
        img_canny = cv.Canny(img_blur, 10, 40)
        ctr, _ = cv.findContours(img_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        print("-----------------------------------------------------------")
        print('PIECE N° : ',i+1)
        print("Number of peices :", len(ctr))
        for cnt2 in ctr:

            cv.drawContours(B[i], ctr, -1, (255, 0, 255), 2)
            area2 = cv.contourArea(cnt2)
            peri2 = cv.arcLength(cnt2, True)
            approx2 = cv.approxPolyDP(cnt2, 0.02 * peri2, True)
            x2, y2, w2, h2 = cv.boundingRect(approx2)
            cv.rectangle(B[i], (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 3)
            nb_point2 = len(approx2)
            if nb_point2 == 3:texte_form2 = 'Tri'
            elif nb_point2 == 4:
                dist2 = w2 / h2
                if dist2 > 0.95 and dist2 < 1.05:texte_form2 = 'Carre'
                else:texte_form2 = 'Rectangle'
            else:texte_form2 = 'Cercle'
            print(texte_form2, ": Largeur=", w2, ",Longueur=", h2, ",Position X=", x2, ",Position Y=", y2,
                  ",Surface=", area2)
            xlist2.append(x2);ylist2.append(y2);alist2.append(area2)
        if xlist==xlist2 and ylist==ylist2 and alist==alist2:
            print("===>  It is a match")
            cv.imwrite('validated_model\ model2 match  N%s.jpg' % (i + 1), B[i])
        else :
            print("===>  It is not a match")

            cv.imwrite('unvalidated_model\ model2 not a match N%s.jpg' % (i+1), B[i])

#Treatement of third model images:
if nb == '3':
    for i in range (0,10):
        xlist3 = [];ylist3 = [];alist3 = [];ct3=0
        C[i] = cv.resize(C[i], None, fx=0.8, fy=0.8, interpolation=cv.INTER_CUBIC)
        img_gray = cv.cvtColor(C[i], cv.COLOR_BGR2GRAY)
        img_blur = cv.GaussianBlur(img_gray, (3, 3), 2)
        img_canny = cv.Canny(img_blur, 10, 40)
        ctr, _ = cv.findContours(img_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        print("-----------------------------------------------------------------")
        print('PIECE N° : ',i+1)
        print("Number of peices:", len(ctr))
        for cnt3 in ctr:

            cv.drawContours(C[i], ctr, -1, (255, 0, 255), 2)
            area3 = cv.contourArea(cnt3)
            peri3 = cv.arcLength(cnt3, True)
            approx3 = cv.approxPolyDP(cnt3, 0.02 * peri3, True)
            x3, y3, w3, h3 = cv.boundingRect(approx3)
            cv.rectangle(C[i], (x3, y3), (x3 + w3, y3 + h3), (0, 255, 0), 3)
            nb_point3 = len(approx3)
            if nb_point3 == 3:texte_form3 = 'Tri'
            elif nb_point3 == 4:
                dist3 = w3 / h3
                if dist3 > 0.95 and dist3 < 1.05:texte_form3 = 'Carre'
                else:texte_form3 = 'Rectangle'
            else:texte_form3 = 'Cercle'
            print(texte_form3, ": Largeur=", w3, ",Longueur=", h3, ",Position X=", x3, ",Position Y=", y3,
                  ",Surface=", area3)
            xlist3.append(x3);ylist3.append(y3);alist3.append(area3)
        if xlist==xlist3 and ylist==ylist3 and alist==alist3:
            print("===> It is a match ")
            cv.imwrite('validated_model\Model3 match N%s.jpg' % (i+1), C[i])
        else :
            print("===> It is not match ")
            cv.imwrite('unvalidated_model\Model3 not a match N%s.jpg' % (i+1), C[i])


print('--------------------------------------------------------')

cv.waitKey(0)
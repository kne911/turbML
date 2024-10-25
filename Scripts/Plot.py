import matplotlib.pyplot as plt
from LoadData import *

def PlotData(yplus_DNS, uu_DNS, vv_DNS, ww_DNS, dudy_DNS, tau_DNS, k_DNS, c_0_DNS, c_2_DNS, c0, c2, index_test, index_train, trainingCase, validationCase):
 
    if index_test is None:
        index_test = range(len(c0))
    if index_train is None:
        index_train = range(len(c0))

    uu_NN, vv_NN, ww_NN = GetStresses(tau_DNS[index_test], dudy_DNS[index_test], k_DNS[index_test], c0, c2)
    
    plt.figure(figsize=(8,6))
    plt.plot(c_0_DNS[index_test], yplus_DNS[index_test],'bo',label='Ground truth')
    plt.plot(c0, yplus_DNS[index_test], 'ro', label='Predictions')
    plt.xlabel("$c_0$")
    plt.ylabel("$y^+$")
    plt.title(f'Training: {trainingCase} \n Validation: {validationCase}')
    plt.legend(loc="best",fontsize=12)
    plt.savefig(f'Output/c0_{trainingCase}_{validationCase}.png')
    
    plt.figure(figsize=(8,6))
    plt.plot(c_2_DNS[index_test], yplus_DNS[index_test],'bo',label='Ground truth')
    plt.plot(c2, yplus_DNS[index_test], 'ro', label='Predictions')
    plt.xlabel("$c_2$")
    plt.ylabel("$y^+$")
    plt.title(f'Training: {trainingCase} \n Validation: {validationCase}')
    plt.legend(loc="upper center",fontsize=12)
    plt.savefig(f'Output/c2_{trainingCase}_{validationCase}.png')
    
    
    fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(10,6), sharey=True)
    # plt.title(f'Training: {trainingCase} \n Validation: {validationCase}')
    fig.suptitle(f'Training: {trainingCase} \n Validation: {validationCase}')
    fig.supylabel('$y^+$')
    ax1.scatter(uu_NN,yplus_DNS[index_test], marker="o", s=10, c="red", label="Predictions")
    ax1.plot(uu_DNS, yplus_DNS, label="Ground truth")
    ax1.legend()
    ax1.set_xlabel("$\overline{u'u'}^+$")
    ax2.scatter(vv_NN,yplus_DNS[index_test], marker="o", s=10, c="red")
    ax2.plot(vv_DNS, yplus_DNS)
    ax2.set_xlabel("$\overline{v'v'}^+$")
    ax3.scatter(ww_NN,yplus_DNS[index_test], marker="o", s=10, c="red")
    ax3.plot(ww_DNS, yplus_DNS)
    ax3.set_xlabel("$\overline{w'w'}^+$")
    plt.savefig(f'Output/stresses_{trainingCase}_{validationCase}.png')

    

    
    # fig1,ax1 = plt.subplots()
    # plt.subplots_adjust(left=0.20,bottom=0.20)
    # for k in range(0,len(X_test)):
    #     k_test = index_test[k]
    #     yplus = yplus_DNS[k_test]
    #     if k == 0: 
    #         plt.plot(c_0_DNS[k_test],yplus, 'bo',label='target')
    #         plt.plot(c0[k],yplus, 'r+',label='NN')
    #     else:
    #         plt.plot(c_0_DNS[k_test],yplus, 'bo')
    #         plt.plot(c0[k],yplus, 'r+')
    # plt.xlabel("$c_0$")
    # plt.ylabel("$y^+$")
    # plt.legend(loc="best",fontsize=12)
    # # plt.savefig('Output/c0-dudy2-and-dudy-2-hidden-9-yplus-2200-dudy-min-eq.4e-4-scale-with-k-eps-units-BL.png')


    ########################## c0 v dudy**2
    # fig1,ax1 = plt.subplots()
    # plt.subplots_adjust(left=0.20,bottom=0.20)
    # dudy2_inverted=scaler_dudy2.inverse_transform(X_test)
    # for k in range(0,len(X_test)):
    #     if k == 0:
    #         plt.plot(c_0_DNS[index_test[k]],dudy_DNS[index_test[k]]**2, 'bo',label='target')
    #         plt.plot(c0[k],dudy2_inverted[k,0], 'r+',label='NN')
    #     else:
    #         plt.plot(c_0_DNS[index_test[k]],dudy_DNS[index_test[k]]**2,'bo')
    #         plt.plot(c0[k],dudy2_inverted[k,0], 'r+')
    # plt.xlabel("$c_0$")
    # plt.ylabel(r"$\left(\partial U/\partial y\right)^2$")
    # plt.legend(loc="best",fontsize=12)
    # plt.savefig('Output/c0-dudu2-dudy2-and-dudy-2-hidden-9-yplus-2200-dudy-min-eq.4e-4-scale-with-k-eps-units-BL.png')


    ########################## c2 v dudy**2
    # fig1,ax1 = plt.subplots()
    # plt.subplots_adjust(left=0.20,bottom=0.20)
    # for k in range(0,len(X_test)):
    #     if k == 0:
    #         plt.plot(c_2_DNS[index_test[k]],dudy_DNS[index_test[k]]**2, 'bo',label='target')
    #         plt.plot(c_NN[k,1],dudy_DNS[index_test[k]]**2, 'r+',label='NN')
    #     else:
    #         plt.plot(c_2_DNS[index_test[k]],dudy_DNS[index_test[k]]**2,'bo')
    #         plt.plot(c_NN[k,1],dudy_DNS[index_test[k]]**2, 'r+')
    # plt.xlabel("$c_2$")
    # plt.ylabel(r"$\left(\partial U/\partial y\right)^2$")
    # plt.legend(loc="best",fontsize=12)
    # plt.savefig('Output/c2-dudu2-dudy2-and-dudy-2-hidden-9-yplus-2200-dudy-min-eq.4e-4-scale-with-k-eps-units-BL.png')


    # ########################## c2
    # fig1,ax1 = plt.subplots()
    # plt.subplots_adjust(left=0.20,bottom=0.20)
    # for k in range(0,len(X_test)):
    #     k_test = index_test[k]
    #     yplus = yplus_DNS[k_test]
    #     if k == 0: 
    #         plt.plot(c_2_DNS[k_test],yplus, 'bo',label='target')
    #         plt.plot(c_NN[k,1],yplus, 'r+',label='NN')
    #     else:
    #         plt.plot(c_2_DNS[k_test],yplus, 'bo')
    #         plt.plot(c_NN[k,1],yplus, 'r+')
    # # ax4.axis([-2000, 0, 0,5000])
    # # ax5.axis([-2000, 0, 0,5000])
    # plt.xlabel("$c_2$")
    # plt.ylabel("$y^+$")
    # plt.legend(loc="best",fontsize=12)
    # plt.savefig('Output/c2-dudy2-and-dudy-2-hidden-9-yplus-2200-dudy-min-eq.4e-4-scale-with-k-eps-units-BL.png')




    # ########################## uu
    # fig1,ax1 = plt.subplots()
    # plt.subplots_adjust(left=0.20,bottom=0.20)
    # ax1.scatter(uu_NN,yplus_DNS_test, marker="o", s=10, c="red", label="Neural Network")
    # ax1.plot(uu_DNS,yplus_DNS,'b-', label="Target")
    # plt.xlabel("$\overline{u'u'}^+$")
    # plt.ylabel("$y^+$")
    # plt.legend(loc="best",fontsize=12)
    # plt.savefig('Output/uu-dudy2-and-dudy-2-hidden-9-yplus-2200-dudy-min-eq.4e-4-scale-with-k-eps-units-BL.png')


    # ########################## vv
    # fig1,ax1 = plt.subplots()
    # plt.subplots_adjust(left=0.20,bottom=0.20)
    # ax1.scatter(vv_NN,yplus_DNS_test, marker="o", s=10, c="red", label="Neural Network")
    # ax1.plot(vv_DNS,yplus_DNS,'b-', label="Target")
    # plt.xlabel("$\overline{v'v'}^+$")
    # plt.ylabel("$y^+$")
    # plt.legend(loc="best",fontsize=12)
    # plt.savefig('vv-dudy2-and-dudy-2-hidden-9-yplus-2200-dudy-min-eq.4e-4-scale-with-k-eps-units-BL.png')

    # ########################## ww
    # fig1,ax1 = plt.subplots()
    # plt.subplots_adjust(left=0.20,bottom=0.20)
    # ax1.scatter(ww_NN,yplus_DNS_test, marker="o", s=10, c="red", label="Neural Network")
    # ax1.plot(ww_DNS,yplus_DNS,'b-', label="Target")
    # plt.xlabel("$\overline{w'w'}^+$")
    # plt.ylabel("$y^+$")
    # plt.legend(loc="best",fontsize=12)
    # plt.savefig('Output/ww-dudy2-and-dudy-2-hidden-9-yplus-2200-dudy-min-eq.4e-4-scale-with-k-eps-units-BL.png')

    # ########################## time scales
    # fig1,ax1 = plt.subplots()
    # plt.subplots_adjust(left=0.20,bottom=0.20)
    # ax1.plot(dudy_DNS_org,yplus_DNS,'r-', label=r"$dudy$")
    # ax1.plot(1/dudy_DNS_org,yplus_DNS,'b-', label=r"$\left(\partial U/\partial y\right)^{-1}$")
    # plt.xlabel("time scsles")
    # plt.ylabel("$y^+$")
    # plt.legend(loc="best",fontsize=12)
    # plt.savefig('Output/time-scales-dudy-and-dudy-squared-dudy2-and-dudy-2-hidden-9-yplus-2200-dudy-min-eq.4e-4-scale-with-k-eps-units-BL.png')

    # ########################## time scales
    # fig1,ax1 = plt.subplots()
    # plt.subplots_adjust(left=0.20,bottom=0.20)
    # ax1.plot(dudy_DNS_org*dudy_DNS_org,yplus_DNS,'b-')
    # plt.xlabel(r"$\left(\partial U/\partial y\right)^{-1} dudy$")
    # plt.ylabel("$y^+$")
    # plt.savefig('Output/dudy-times-dudy-dudy-and-dudy-squared-dudy2-and-dudy-2-hidden-9-yplus-2200-dudy-min-eq.4e-4-scale-with-k-eps-units-BL.png')

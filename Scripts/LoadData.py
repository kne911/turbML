import numpy as np

def GetInputData(case: str, minYplus, maxYplus, maxDudy = 4e-4):
    if case == 'BoundaryLayer':
        vel_DNS=np.genfromtxt("../Data/vel_11000_DNS_no-text.dat", comments="%")
        bud_DNS=np.genfromtxt("../Data/bud_11000.prof", comments="%")
       
        y_DNS       = vel_DNS[:,0]
        yplus_DNS   = vel_DNS[:,1]
        u_DNS       = vel_DNS[:,2]
        uu_DNS      = vel_DNS[:,3]**2
        vv_DNS      = vel_DNS[:,4]**2
        ww_DNS      = vel_DNS[:,5]**2
        uv_DNS      = vel_DNS[:,6]
        eps_DNS     = bud_DNS[:,4]
        
    elif case == 'FullyDevelopedChannel_Re550':
        vel_DNS=np.genfromtxt("../Data/Re550.dat", comments="%")
        input_DNS=np.genfromtxt("../Data/Re550_bal_kbal.dat", comments="%")
        
        y_DNS       = vel_DNS[:,0]
        yplus_DNS   = vel_DNS[:,1]
        u_DNS       = vel_DNS[:,2]
        uu_DNS      = vel_DNS[:,3]**2
        vv_DNS      = vel_DNS[:,4]**2
        ww_DNS      = vel_DNS[:,5]**2
        uv_DNS      = vel_DNS[:,10]
        eps_DNS     = input_DNS[:, 2]
        
        
    elif case == 'FullyDevelopedChannel_Re5200':
        input_mean      = np.genfromtxt("../Data/LM_Channel_5200_mean_prof.dat",comments="%")
        input_DNS       = np.genfromtxt("../Data/LM_Channel_5200_vel_fluc_prof.dat", comments="%")
        input_RSTE_k    = np.genfromtxt("../Data/LM_Channel_5200_RSTE_k_prof.dat", comments="%")
        
        y_DNS       = input_mean[:, 0]
        yplus_DNS   = input_mean[:, 1]
        u_DNS       = input_mean[:, 2]
        y_DNS       = input_DNS[:, 0]
        yplus_DNS   = input_DNS[:, 1]
        uu_DNS      = input_DNS[:, 2]
        vv_DNS      = input_DNS[:, 3]
        ww_DNS      = input_DNS[:, 4]
        uv_DNS      = input_DNS[:, 5]
        eps_DNS     = input_RSTE_k[:, 7]
    else:
        raise Exception('Case not found. Choose one of the following: \n \'BoundaryLayer\' \n \'FullyDevelopedChannel_Re550\' \n \'FullyDevelopedChannel_Re5200\'')
    
    k_DNS = 0.5 * (uu_DNS + vv_DNS + ww_DNS)  
    dudy_DNS  = np.gradient(u_DNS,yplus_DNS)
    dudy_DNS = np.maximum(dudy_DNS, maxDudy)
    mask = np.nonzero((yplus_DNS > minYplus) & (yplus_DNS < maxYplus))
    
    print('Returning data from: ' + case + '. Min yplus: ' + str(minYplus) + '. Max yplus: ' + str(maxYplus))

    return y_DNS[mask], yplus_DNS[mask], u_DNS[mask], uu_DNS[mask], vv_DNS[mask], ww_DNS[mask], uv_DNS[mask], k_DNS[mask], eps_DNS[mask], dudy_DNS[mask]

def GetC0andC2(k_DNS, eps_DNS, dudy_DNS, uu_DNS, vv_DNS, ww_DNS):

    # Calculate ny_t and time-scale tau
    #viscous_t = k_DNS**2/eps_DNS 
    # tau       = viscous_t/abs(uv_DNS)
    tau_DNS = k_DNS/eps_DNS
    a11_DNS=uu_DNS/k_DNS-0.66666
    #a22_DNS=vv_DNS/k_DNS-0.66666
    a33_DNS=ww_DNS/k_DNS-0.66666

    c_2_DNS=(2*a11_DNS+a33_DNS)/tau_DNS**2/dudy_DNS**2
    c_0_DNS=-6*a33_DNS/tau_DNS**2/dudy_DNS**2

    c = np.array([c_0_DNS,c_2_DNS])
    
    print('Returning c = [c0, c2], a11 and a33')
    return c, a11_DNS, a33_DNS

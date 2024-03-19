# MONTHLY MEAN ANOMALY
# Restituisce un nuovo dataset in cui in ogni cella c'è la differenza
# tra il mese selezionato e la media di quello stesso mese nell'intero intervallo

# _mm = Monthly Mean
sst_mm = ds.groupby('time.month').mean('time')
sst_anom = ds.groupby('time.month') - sst_mm




# DETRENDING
p = ds.polyfit(dim='time', deg=xxx)
fit = xr.polyval(ds['time'], p.polyfit_coefficients)
sst_detr= ds - fit


# Oppure:
def detrend_dim(da, dim, deg=1):
    p = da.polyfit(dim=dim, deg=deg)
    fit = xr.polyval(da[dim], p.polyfit_coefficients)
    return da - fit
# per usarla:
sst_detr=detrend_dim(ds,'xxx',deg=xxx)





# PDF
# Sostituire AAAAA con il dataset che vogliamo (p.es. ds1)

bins=np.arange(valore_min,valore_nax,incremento)
histhr, bin_edges = np.histogram(AAAAA, bins, density=True)
bin_center=(bin_edges[0:-1]+bin_edges[1:])/2

fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(xxx,xxx))
ax.plot(bin_center,histhr,'colore',label='legenda')
ax.grid()
ax.legend()
plt.title('Titolo PDF')




# POWER SPECTRUM
# Sostituire AAAAA con il dataset che vogliamo (p.es. ds1)

L=len(AAAAA)
LPS=int((L/2))
Lyr=L/12
prds_yrs=Lyr/np.arange(1,LPS)
sfft_all=np.fft.fft(AAAAA)
sfft=sfft_all[1:LPS]

sfft_amp=2*sfft/L
psp=np.abs(sfft_amp)

fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(10, 5))
ax.plot(prds_yrs,psp,'.-')
ax.title.set_text('s_fft norm. to get amplitudes in '+dse['sst'].units)
ax.set_ylabel(dse['sst'].units)
ax.set_xlabel('time in years')
plt.xlim(right=20)
plt.xlim(left=0)

df_psp = pd.DataFrame(psp)
psp_mavg=df_psp.rolling(7, center=True).mean()
ax.plot(prds_yrs,psp_mavg,'r')



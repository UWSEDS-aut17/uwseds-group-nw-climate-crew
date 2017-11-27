#==========================================#
# Reconstructing the Fish Model            #
#==========================================#

##=== Reading in Data
Temp <-read.csv("Temp_GrowthR.csv", header=TRUE)
Flow <-read.csv("Flow_SpawnArea.csv", header=TRUE)

##=== Temperature Model
head(Temp)
# Beta Function & Parameters
BetaTemp <-function(Temp){Rmax*((Tmax-Temp)/(Tmax-Topt))*((Temp-Tmin)/(Topt-Tmin))^((Topt-Tmin)/(Tmax-Topt))}
Rmax <-3.25; Tmax <-25; Tmin <--5; Topt <-17.6
# Figure
pdf("Temp_Mod.pdf", width=4, height=4)
par(oma=c(1,1,1,1), mar=c(4,3,1,1))
plot(Temp$Temp, Temp$GrowthR, xlim=c(10,25), ylim=c(0,3.5), axes=F, ann=F); box()
par(new=TRUE)
curve(BetaTemp, from=10, to=25, n=1000, xlim=c(10,25), ylim=c(0,3.5),
      ann=F, axes=F, lwd=1.5)
axis(side=1, at=seq(0,25,5), labels=seq(0,25,5), cex.axis=1.2, tck=0.02)
axis(side=2, at=seq(0,3,1), labels=seq(0,3,1), 
     las=2, tck=0.01, hadj=0.6, cex.axis=1.2)
title(x=expression(paste("Stream Temperature (", degree, "C)")), cex.lab=1, font.lab=1, line=2.5)
title(y="Growth Rate (% weight / day)", cex.lab=1, line=1.8)
dev.off()

##=== Stream Flow Mod
# Chinook
Chinook <-Flow[which(Flow$Species=="Chinook"),]
Fo <-424; a <-12818; b <-424
Flow <-seq(0,1500,1)
Chinook_Area <-a/(1+((Flow-Fo)/b)^2)
# Sockeye
Sockeye <-Flow[which(Flow$Species=="Sockeye"),]
Fo <-390; a <-946; b <-390
Flow <-seq(0,1500,1)
Sockeye_Area <-a/(1+((Flow-Fo)/b)^2)
# Coho
Coho <-Flow[which(Flow$Species=="Coho"),]
Fo <-362; a <-12124; b <-362
Flow <-seq(0,1500,1)
Coho_Area <-a/(1+((Flow-Fo)/b)^2)
# Pink
Pink <-Flow[which(Flow$Species=="Pink"),]
Beta_Pink <-function(Flow){Amax*((Fmax-Flow)/(Fmax-Fopt))*((Flow-Fmin)/(Fopt-Fmin))^((Fopt-Fmin)/(Fmax-Fopt))}
Amax <-1052; Fmax <-1200; Fmin <-0; Fopt <-420

# Figure
pdf("Flow_Mod.pdf", width=6, height=6)
par(mfrow=c(2,2), oma=c(1,1,1,1))

par(mar=c(4,4,1,1))
plot(Chinook$StreamFlow, Chinook$SpawnArea, 
     xlim=c(0,1500), ylim=c(3000,15000), ann=F, axes=F); box()
axis(side=1, at=seq(0,1500,500), labels=seq(0,1500,500), cex.axis=1, tck=0.02)
axis(side=2, at=seq(0,15000,5000), labels=seq(0,15,5), las=2, tck=0.01, hadj=0.6, cex.axis=1)
title(x="Stream Flow (cubic feet / sec)", cex.lab=1, font.lab=1, line=2.2)
title(y="Spawnable Area \n(1,000 square feet)", cex.lab=1, line=1.8)
par(new=TRUE)
plot(Chinook_Area, type="l", xlim=c(0,1500), ylim=c(3000,15000), ann=F, axes=F)
text(300, 14500, "Chinook")

par(mar=c(4,4,1,1))
plot(Sockeye$StreamFlow, Sockeye$SpawnArea, 
     xlim=c(150,900), ylim=c(200,1100), ann=F, axes=F); box()
axis(side=1, at=seq(0,1000,200), labels=seq(0,1000,200), cex.axis=1, tck=0.02)
axis(side=2, at=seq(0,1000,200), labels=seq(0,1000,200), las=2, tck=0.01, hadj=0.6, cex.axis=1)
title(x="Stream Flow (cubic feet / sec)", cex.lab=1, font.lab=1, line=2.2)
title(y="Spawnable Area (square feet)", cex.lab=1, line=2.5)
par(new=TRUE)
plot(Sockeye_Area, type="l", xlim=c(150,900), ylim=c(200,1100), ann=F, axes=F)
text(300, 1050, "Sockeye")

par(mar=c(4,4,1,1))
plot(Coho$StreamFlow, Coho$SpawnArea, 
     xlim=c(100,900), ylim=c(3000,15000), ann=F, axes=F); box()
axis(side=1, at=seq(0,1000,200), labels=seq(0,1000,200), cex.axis=1, tck=0.02)
axis(side=2, at=seq(3000,13000,2000), labels=seq(3,13,2), las=2, tck=0.01, hadj=0.6, cex.axis=1)
title(x="Stream Flow (cubic feet / sec)", cex.lab=1, font.lab=1, line=2.2)
title(y="Spawnable Area \n(1,000 square feet)", cex.lab=1, line=1.8)
par(new=TRUE)
plot(Coho_Area, type="l", xlim=c(100,900), ylim=c(3000,15000), ann=F, axes=F)
text(250, 14300, "Coho")

par(mar=c(4,4,1,1))
plot(Pink$StreamFlow, Pink$SpawnArea, xlim=c(100,900), ylim=c(300,1200), ann=F, axes=F); box()
axis(side=1, at=seq(100,1000,200), labels=seq(100,1000,200), cex.axis=1, tck=0.02)
axis(side=2, at=seq(0,1200,300), labels=seq(0,1200,300), las=2, tck=0.01, hadj=0.6, cex.axis=1)
title(x="Stream Flow (cubic feet / sec)", cex.lab=1, font.lab=1, line=2.2)
title(y="Spawnable Area (square feet)", cex.lab=1, line=2.5)
par(new=TRUE)
curve(Beta_Pink, from=0, to=1000, n=1000, 
      xlim=c(100,900), ylim=c(300,1200), ann=F, axes=F, lwd=1)
text(200, 1160, "Pink")

dev.off()
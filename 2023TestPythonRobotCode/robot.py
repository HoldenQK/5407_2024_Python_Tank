#Robotics Practice Robot

#Imported Libraries
import rev
import wpilib
import wpilib.drive
import wpilib.interfaces
import wpilib.event



class robot(wpilib.TimedRobot):
    def robotInit(self):
#Ports
        self.left_motor_port = 7 
        self.left_motor_port2 = 4
        self.right_motor_port = 5 
        self.right_motor_port2 = 1
        self.xbox_controler_port = 0 
#Drive Motors
        self.left_motor = rev.CANSparkMax(self.left_motor_port, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.right_motor = rev.CANSparkMax(self.right_motor_port, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.left_motor2 = rev.CANSparkMax(self.left_motor_port2, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.right_motor2 = rev.CANSparkMax(self.right_motor_port2, rev._rev.CANSparkLowLevel.MotorType.kBrushless)
        self.left_motor_group = wpilib.MotorControllerGroup(self.left_motor, self.left_motor2)
        self.right_motor_group = wpilib.MotorControllerGroup(self.right_motor, self.right_motor2)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor_group, self.right_motor_group)

#Speed Ratio
        #self.Speed_Mode = [1, 0.75,0.5,0.25,0]
        #self.SPV = 0
        self.TurnRatio = 1

#Xbox Input 
        self.controler = wpilib.XboxController(self.xbox_controler_port)
        #self.Xbox_A_Button = wpilib.XboxController.getAButton(self.controler)
        #self.Xbox_B_Button = wpilib.XboxController.getBButton(self.controler)
        #self.Xbox_X_Button = wpilib.XboxController.getXButton(self.controler)
        #self.Xbox_Y_Button = wpilib.XboxController.getYButton(self.controler)
        #self.Xbox_Start_Button = wpilib.XboxController.getStartButton(self.controler)
        self.Xbox_Left_JoyStick_Y = self.controler.getLeftY()
        self.Xbox_Left_JoyStick_X = self.controler.getLeftX()
        #self.Xbox_Left_Trigger = wpilib.XboxController.getLeftBumper(self.controler)
        #self.Xbox_Right_Trigger = wpilib.XboxController.getRightBumper(self.controler)

    def teleopExit(self):

        self.drive.stopMotor()


    def teleopPeriodic(self):

        #if (self.Xbox_Left_Trigger == True and self.SPV > 0):
                #self.SPV -= 1
        #elif (self.Xbox_Right_Trigger == True and self.SPV < len(self.Speed_Mode)-1):
                #self.SPV += 1

        self.drive.tankDrive(
                 self.Xbox_Left_JoyStick_Y + (self.Xbox_Left_JoyStick_X * self.TurnRatio) ,
                 self.Xbox_Left_JoyStick_Y - (self.Xbox_Left_JoyStick_X * self.TurnRatio) )


if __name__ == "__main__":
    wpilib.run(robot)


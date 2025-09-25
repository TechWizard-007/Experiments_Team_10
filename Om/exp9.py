# rigid
import pybullet as p
import pybullet_data
import time
import random

def spawn_box(pos, size=(0.1,0.1,0.1), mass=1.0):
    coll_shape = p.createCollisionShape(p.GEOM_BOX, halfExtents=[s/2 for s in size])
    vis_shape = p.createVisualShape(p.GEOM_BOX, halfExtents=[s/2 for s in size])
    body = p.createMultiBody(baseMass=mass, baseCollisionShapeIndex=coll_shape,
                             baseVisualShapeIndex=vis_shape, basePosition=pos)
    
    p.resetBaseVelocity(body, angularVelocity=[random.uniform(-5,5) for _ in range(3)],
                        linearVelocity=[random.uniform(-1,1) for _ in range(3)])
    return body

def main():
    
    physicsClient = p.connect(p.GUI)  
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.81)
    plane = p.loadURDF("plane.urdf")

    
    parent = spawn_box([0, 0, 1.2], size=(0.5,0.5,0.1), mass=5.0)

    
    debris = []
    n = 60
    for i in range(n):
        x = random.uniform(-0.4, 0.4)
        y = random.uniform(-0.4, 0.4)
        z = 1.0 + random.uniform(0, 0.4)
        sz = (random.uniform(0.05,0.15),)*3
        debris.append(spawn_box([x,y,z], size=sz, mass=random.uniform(0.2,1.0)))

    for step in range(2000):
        p.stepSimulation()
        time.sleep(1./240.)
    
    p.disconnect()

if __name__ == "__main__":
    main()
extends Node2D

@onready var door: Area2D = $Door
@onready var enemy: Node2D = $EnemyB

func _ready() -> void:
	$Key.collected.connect(on_key_collected)
	$Door.entered.connect(on_door_entered)
	$Gem.collected.connect(on_gem_collected)
	
func on_key_collected():
	door.open()
 
func on_door_entered():
	pass

func on_gem_collected():
	enemy.can_be_hurt()

.globl _start
_start:
	.thumb
	.align 2
	mov ip, r5
	
	add r5, pc, #20
	
	ldr r5, [r5]
	
	push {r5}
	
	mov r5, ip

	push {r0}
	
	add r0, sp, #4

	ldr r0, [r0]

	mov ip, r0

	mov ip, ip
	
	pop {r0}
	
	pop {pc}

	mov ip, ip
	mov ip, ip	
	
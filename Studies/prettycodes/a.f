      PROGRAM MomentosUniformes
      ivezes=0
      rmedia=0
      WRITE (*,*) "Quantidade de numeros aleatórios (N)"
      READ (*,*) N
      WRITE (*,*) "Escolha o momento estátistico (1,2,3,4...)"
      READ (*,*) momento
      DO WHILE (ivezes<N)
        rmedia=rmedia+ RAND()**momento
        ivezes=ivezes+1
      END DO
      WRITE(*,*) rmedia/N
      END PROGRAM      

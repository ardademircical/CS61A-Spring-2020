;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car(cddr s))
)

(define (sign x)
    (cond
        ((> x 0) 1)
        ((< x 0) -1)
        (else 0))
)

(define (square x) (* x x))

(define (pow b n)
    (if (= n 0)
        1
        (if (even? n)
            (pow (square b) (/ n 2))
            (* b (pow b (- n 1))))
        )
)

(define (unique s)
    (if (null? s)
        s
        (car (cdr s))
    )
)
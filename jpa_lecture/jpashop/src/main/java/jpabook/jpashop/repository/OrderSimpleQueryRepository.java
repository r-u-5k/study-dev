package jpabook.jpashop.repository;

import jakarta.persistence.EntityManager;
import jpabook.jpashop.domain.OrderSimpleQueryDto;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@RequiredArgsConstructor
public class OrderSimpleQueryRepository {
    private final EntityManager em;

    public List<OrderSimpleQueryDto> findOrderDtos() {
        List<OrderSimpleQueryDto> resultList = em.createQuery("select new jpabook.jpashop.domain.OrderSimpleQueryDto" +
                "(o.id, m.name, o.orderDate, o.status, d.address) from Order o" +
                " join o.member m" +
                " join o.delivery d", OrderSimpleQueryDto.class).getResultList();
        return resultList;
    }
}
